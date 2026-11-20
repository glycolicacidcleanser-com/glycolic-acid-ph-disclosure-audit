# Glycolic acid pH disclosure audit

A dated snapshot of whether glycolic acid skincare brands publish the pH of their formulas on their own product pages. Compiled by Rodger, editor, [glycolicacidcleanser.com](https://glycolicacidcleanser.com/glycolic-acid-statistics/#disclosure-gap).

The percentage on a glycolic acid label tells you how much glycolic acid is in the formula. How much of it is in the free, un-ionised form depends on the formula's pH, so a percentage without a pH is half the information.

**Read it as a page:** [glycolicacidcleanser-com.github.io/glycolic-acid-ph-disclosure-audit](https://glycolicacidcleanser-com.github.io/glycolic-acid-ph-disclosure-audit/) (the table, the figures and the method, generated from the CSV).

## What is in this repository

| File | What it is |
|---|---|
| `data/ph-disclosure-audit-2026-09.csv` | One row per brand and product audited on 5 September 2026 (31 rows) |
| `README.md` | This file: method, columns, status codes and caveats |
| `docs/index.html` | The same data as a web page, built by `tools/build_page.py`; do not edit by hand |

## Headline figures

- 31 brands were tracked on 5 September 2026, each with one glycolic acid product sold on Amazon US.
- 26 of them had a product page that could be read. Of those 26, **8 publish a numeric pH (31%)**.
- 13 raise pH at all. **5 of those give no number**: they use wording such as "pH-balanced" or "pH optimized", or call the pH proprietary.
- Of the 8 that publish a number, 6 give a range rather than a single value.

The five rows that are not in the 26 are excluded from the denominator: three products that are not on the brand's own site, one tracked name that is only a storefront wrapper, and one shop that had closed.

## Columns

| Column | Meaning |
|---|---|
| `brand` | Brand name as it appears on the product page |
| `product` | The product audited |
| `status` | Disclosure category, defined below |
| `ph_value` | The pH exactly as the brand states it, including any range; empty when none is stated |
| `source_url` | The brand's own page that was checked |
| `note` | What was found, in a few words, and any re-verification date |

## Status codes

| Code | Meaning |
|---|---|
| `PH_PUBLISHED` | The brand's page states a numeric pH |
| `CLAIM_NO_NUMBER` | The page makes a pH claim ("pH-balanced") but gives no number |
| `NO_PH_ON_PAGE` | The page was read and says nothing about pH |
| `PH_PROVIDED_ON_REQUEST` | The page says nothing about pH, but the brand gave a figure when we asked by email. Added after the 5 September audit (one row, 15 November 2026); not counted among the 8 published pH values |
| `PRODUCT_NOT_ON_BRAND_SITE` | The product could not be found on the brand's own site; excluded from the 26 |
| `NO_BRAND_SITE` | There is no brand site, only a storefront wrapper; excluded from the 26 |
| `NOT_TRADING` | The shop had closed; excluded from the 26 |

## Method

1. For each tracked product, the brand's own website was read on 5 September 2026.
2. A pH counts as published only when the brand's own page states it as a number. Marketing language alone is recorded as `CLAIM_NO_NUMBER`.
3. Where a value was re-checked or added on a later date, the note says so. The one row added after 5 September is YEOUTH, from a customer-service reply of 15 November 2026. One brand's site blocks automated reading, so its value was read by hand from a browser session; the note says that too.

### Free acid, for readers who want to compute it

The share of glycolic acid left un-ionised at a given pH comes from the Henderson-Hasselbalch equation at glycolic acid's pKa of 3.83:

```
free acid (%) = label percentage ÷ (1 + 10^(pH − 3.83))
```

This is theoretical arithmetic from a stated pH, not a lab measurement. Heavily buffered or time-release formulas can deviate. The method for estimating free acid at a given pH was published by cosmetic chemist Michelle Wong at [Lab Muffin Beauty Science](https://labmuffin.com/free-acid-calculator-for-exfoliants-at-specific-ph-levels/); what this audit adds is each brand's own published pH.

## Caveats

- This is a snapshot from 5 September 2026. Brands change their pages, and it has not been recomputed since.
- It covers one product per brand, not each brand's whole range.
- The set is brands selling glycolic acid products on Amazon US, not the whole market.
- Publishing a pH range is not the same as publishing the strength: a range of pH 3.4 to 4.0 on an 8% product spans roughly 3.2% to 5.8% free acid.

## Licence and credit

The compilation is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reuse it with credit to glycolicacidcleanser.com and a link to the [statistics page](https://glycolicacidcleanser.com/glycolic-acid-statistics/). The licence covers the compilation only, not the brands' own text.

## Corrections

If a brand's pH is wrong or out of date, open an issue on this repository with the page that shows it. A verified correction is fixed and dated.
