#!/usr/bin/env python3
"""Build docs/index.html from data/ph-disclosure-audit-2026-09.csv. Run from the repository root: python3 tools/build_page.py
The page is generated so the table cannot drift from the CSV."""
import csv, html, json, collections

CSV = "data/ph-disclosure-audit-2026-09.csv"
SITE = "https://glycolicacidcleanser.com"
PAGE = "https://glycolicacidcleanser-com.github.io/glycolic-acid-ph-disclosure-audit/"
REPO = "https://github.com/glycolicacidcleanser-com/glycolic-acid-ph-disclosure-audit"
LABEL = {
    "PH_PUBLISHED": "pH published",
    "CLAIM_NO_NUMBER": "pH claim, no number",
    "NO_PH_ON_PAGE": "no pH on the page",
    "PRODUCT_NOT_ON_BRAND_SITE": "product not on the brand's site",
    "NO_BRAND_SITE": "no brand site",
    "NOT_TRADING": "shop closed",
}
rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
c = collections.Counter(r["status"] for r in rows)
excluded = c["PRODUCT_NOT_ON_BRAND_SITE"] + c["NO_BRAND_SITE"] + c["NOT_TRADING"]
readable = len(rows) - excluded
published = c["PH_PUBLISHED"]
e = html.escape

def tr(r):
    src = f'<a href="{e(r["source_url"])}" rel="noopener">brand page</a>' if r["source_url"].startswith("http") else ""
    return (f'<tr class="s-{r["status"].lower()}"><td>{e(r["brand"])}</td><td>{e(r["product"])}</td>'
            f'<td>{e(LABEL.get(r["status"], r["status"]))}</td><td>{e(r["ph_value"]) or "&mdash;"}</td><td>{src}</td><td>{e(r["note"])}</td></tr>')

ld = {
    "@context": "https://schema.org", "@type": "Dataset",
    "name": "Glycolic Acid pH Disclosure Audit (2026-09)",
    "description": f"Brand-by-brand audit of whether {len(rows)} glycolic acid skincare brands publish the pH of their formulas on their own product pages, read on 5 September 2026. {published} of the {readable} readable brand pages state a numeric pH.",
    "url": PAGE, "dateCreated": "2026-09-05", "license": "https://creativecommons.org/licenses/by/4.0/",
    "creator": {"@type": "Organization", "name": "glycolicacidcleanser.com", "url": SITE + "/"},
    "isBasedOn": SITE + "/glycolic-acid-statistics/",
    "sameAs": [REPO, "https://huggingface.co/datasets/glycolicacidcleansercom/glycolic-acid-ph-disclosure-audit"],
    "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv",
                      "contentUrl": "https://raw.githubusercontent.com/glycolicacidcleanser-com/glycolic-acid-ph-disclosure-audit/master/data/ph-disclosure-audit-2026-09.csv"}],
    "variableMeasured": ["brand", "product", "status", "ph_value", "source_url", "note"],
}
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Glycolic Acid pH Disclosure Audit: which brands publish their pH</title>
<meta name="description" content="A dated, open dataset: {published} of {readable} glycolic acid skincare brands state a numeric pH on their own product page. Every brand, product, pH and source, as read on 5 September 2026.">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--bg:#fbfaf6;--fg:#1f2a24;--mut:#5b6660;--line:#d9d6cb;--acc:#1f6b4a;--hi:#e7f1ea}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151a17;--fg:#e8ebe6;--mut:#a3ada7;--line:#2f3a34;--acc:#7fd0a6;--hi:#1e2a24}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1060px;margin:0 auto;padding:28px 16px 56px}}h1{{font-size:1.75rem;line-height:1.25;margin:0 0 8px}}h2{{font-size:1.2rem;margin:32px 0 8px}}
p,li{{max-width:72ch}}a{{color:var(--acc)}}.by{{color:var(--mut);margin:0 0 20px}}
.fig{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:16px 0;padding:0;list-style:none}}
.fig li{{border:1px solid var(--line);border-radius:8px;padding:12px;max-width:none}}.fig b{{display:block;font-size:1.6rem}}
.wrap{{overflow-x:auto;border:1px solid var(--line);border-radius:8px}}table{{border-collapse:collapse;width:100%;min-width:760px;font-size:.92rem}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}th{{background:var(--hi)}}tr.s-ph_published td:nth-child(4){{font-weight:600}}
code{{background:var(--hi);padding:2px 6px;border-radius:4px}}footer{{margin-top:36px;color:var(--mut);font-size:.9rem}}
</style>
</head>
<body>
<main>
<h1>Glycolic acid pH disclosure audit</h1>
<p class="by">Compiled by Rodger, editor, <a href="{SITE}/">glycolicacidcleanser.com</a> &middot; read on 5 September 2026 &middot; <a href="https://creativecommons.org/licenses/by/4.0/" rel="license noopener">CC BY 4.0</a></p>
<p>The percentage on a glycolic acid label says how much glycolic acid is in the formula. How much of it is in the free, un-ionised form depends on the formula's pH, so a percentage without a pH is half the information. This page records, brand by brand, whether the maker publishes that pH on its own product page.</p>
<ul class="fig">
<li><b>{published} of {readable}</b>readable brand pages state a numeric pH</li>
<li><b>{c["CLAIM_NO_NUMBER"]}</b>make a pH claim such as "pH-balanced" and give no number</li>
<li><b>{c["NO_PH_ON_PAGE"]}</b>say nothing about pH</li>
<li><b>{len(rows)}</b>brands tracked; {excluded} could not be read on a brand site and are left out of the {readable}</li>
</ul>
<p>The full analysis, including what a published pH range does and does not tell a shopper, is on the <a href="{SITE}/glycolic-acid-statistics/">glycolic acid statistics page</a>. To turn a label percentage and a pH into an estimated free acid figure, use the <a href="{SITE}/glycolic-acid-percentage-guide/#calculator">free acid calculator</a>.</p>
<h2>The data</h2>
<div class="wrap"><table>
<thead><tr><th>Brand</th><th>Product</th><th>Disclosure</th><th>pH as stated</th><th>Source</th><th>Note</th></tr></thead>
<tbody>
{chr(10).join(tr(r) for r in rows)}
</tbody></table></div>
<p>Download: <a href="{REPO}/blob/master/data/ph-disclosure-audit-2026-09.csv">the CSV on GitHub</a>, or the <a href="{SITE}/data/ph-disclosure-audit-2026-09.csv">same file on glycolicacidcleanser.com</a>.</p>
<h2>Method</h2>
<ol>
<li>For each tracked product, the brand's own website was read on 5 September 2026.</li>
<li>A pH counts as published only when the brand's own page states it as a number. Marketing language alone is recorded as a claim with no number.</li>
<li>Where a value was re-checked on a later date, the note says so.</li>
</ol>
<p>Free acid at a stated pH follows the Henderson-Hasselbalch equation at glycolic acid's pKa of 3.83: <code>free acid (%) = label % &divide; (1 + 10^(pH &minus; 3.83))</code>. This is arithmetic from a stated pH, not a lab measurement. The method was published by cosmetic chemist Michelle Wong at <a href="https://labmuffin.com/free-acid-calculator-for-exfoliants-at-specific-ph-levels/" rel="noopener">Lab Muffin Beauty Science</a>; what this audit adds is each brand's own published pH.</p>
<h2>Caveats</h2>
<ul>
<li>A snapshot from 5 September 2026. Brands change their pages, and it has not been recomputed since.</li>
<li>One product per brand, not each brand's whole range.</li>
<li>Brands selling glycolic acid products on Amazon US, not the whole market.</li>
</ul>
<h2>Reuse and corrections</h2>
<p>Licensed CC BY 4.0: reuse it with credit to glycolicacidcleanser.com and a link to the <a href="{SITE}/glycolic-acid-statistics/">statistics page</a>. The licence covers the compilation, not the brands' own text. If a brand's pH is wrong or out of date, <a href="{REPO}/issues">open an issue</a> with the page that shows it.</p>
<footer>Source and history: <a href="{REPO}">{REPO.replace("https://","")}</a></footer>
</main>
</body>
</html>
"""
open("docs/index.html", "w", encoding="utf-8").write(page)
print(f"rows {len(rows)} · readable {readable} · published {published} · claim-no-number {c['CLAIM_NO_NUMBER']} · no-pH {c['NO_PH_ON_PAGE']}")
