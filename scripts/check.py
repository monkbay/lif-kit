#!/usr/bin/env python3
"""Invariants for lif-kit. Run before every release: python3 scripts/check.py"""
import json,glob,os,re,sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
fail=[]
def need(cond,msg):
    if not cond: fail.append(msg)

pj=json.load(open(".claude-plugin/plugin.json")); mk=json.load(open(".claude-plugin/marketplace.json"))
need(pj["version"]==mk["plugins"][0]["version"],
     "version mismatch plugin.json vs marketplace.json — the plugin cache is keyed by version, so operators would keep the old copy")
need(f'lif-kit@{mk["name"]}' in open("README.md").read(),"README install line does not match marketplace name")

CMDS=["preview","needs-me","proof","track","brief"]
for c in CMDS:
    f=f"skills/{c}/SKILL.md"; need(os.path.exists(f),f"missing {f}")
    if not os.path.exists(f): continue
    t=open(f).read(); fm=t.split("---\n")[1]
    d=dict(re.findall(r"^([a-z-]+):\s*(.+)$",fm,re.M))
    need(d.get("name")==c,f"{f}: name != folder")
    need(len(d.get("description",""))<=1024,f"{f}: description too long")
    need("model:" not in fm,f"{f}: model pin — an account without that model should not error")
    need("## Non-negotiables" in t,f"{f}: rules must survive if operator-kit is not loaded")
    need("## If something is missing" in t,f"{f}: no degraded-mode section")
    nums=re.findall(r"^(\d+)\.",t,re.M)
    need(len(nums)==len(set(nums)),f"{f}: duplicate step numbers")
    need(nums==sorted(nums,key=int),f"{f}: steps out of order")

core=open("skills/operator-kit/SKILL.md").read()
for must,why in [("When this does not apply","stand-down rules stop it hijacking ordinary work"),
                 ("Preflight","must state what it is connected to"),
                 ("Working degraded","must never invent when a tool is missing"),
                 ("hard limits","credentials, money, acting for a person, bulk writes")]:
    need(must in core,f"operator-kit: missing '{must}' — {why}")
for ref in set(re.findall(r"`references/([a-z-]+\.md)`","".join(open(f).read() for f in glob.glob("skills/**/SKILL.md",recursive=True)))):
    need(os.path.exists("skills/operator-kit/references/"+ref),f"missing reference {ref}")

blob="".join(open(f,errors="ignore").read() for f in glob.glob("**/*.md",recursive=True) if ".git" not in f)
need(not re.search(r"\bcredits?\b(?!.*(Never|never|No credit))",blob.replace("no credit figures","")) or
     len([1 for m in re.finditer(r"\bcredits?\b",blob)])<=3, "credits leaked back into operator-facing text")
need("Thanh" not in blob,"an individual is named in a repo the partner clones")
need(not re.search(r"(sk-[A-Za-z0-9]{10,}|Bearer [A-Za-z0-9]{10,})",blob),"possible secret in repo")

print(f"{len(fail)} problem(s)")
[print("  ✘",m) for m in fail]
sys.exit(1 if fail else 0)
