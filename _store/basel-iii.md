---
aid: basel-iii
name: Basel III
description: Basel III is a comprehensive global regulatory framework developed by the Basel Committee on Banking Supervision (BCBS) in response to the 2007-2008 financial crisis. It strengthens bank capital requirements by requiring higher quality and quantity of capital (CET1, Tier 1, Total Capital), introduces new liquidity standards (LCR and NSFR), adds a leverage ratio backstop, and includes countercyclical capital buffers and G-SIB surcharges. Basel III implementation in the EU/UK is delivered via CRD IV/V and CRR regulations. The final Basel III package (sometimes called Basel IV) addresses output floor and credit risk model constraints introduced in 2017.
type: Index
x-type: standard
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking Regulation
  - Basel III
  - Capital Adequacy
  - Capital Requirements
  - Compliance
  - Finance
  - Liquidity
  - Risk Management
url: https://raw.githubusercontent.com/api-evangelist/basel-iii/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.bis.org/bcbs/basel3.htm
    name: Basel III Framework (BIS)
  - type: Website
    url: https://www.eba.europa.eu/regulation-and-policy/own-funds-and-eligible-liabilities
    name: European Banking Authority - Own Funds
  - type: Website
    url: https://www.federalreserve.gov/supervisionreg/Basel.htm
    name: Federal Reserve - Basel Implementation
  - type: Website
    url: https://www.pra.boe.co.uk/pages/policy/crr
    name: UK PRA - CRR Implementation
  - type: Website
    url: https://www.bis.org/bcbs/publ/d424.htm
    name: Basel III Final Package (Dec 2017)
  - type: Website
    url: https://www.bis.org/publ/bcbs189.htm
    name: Basel III Framework Document (Jun 2011)
  - type: Website
    url: https://www.bis.org/publ/bcbs238.htm
    name: Liquidity Coverage Ratio (Jan 2013)
  - type: Website
    url: https://www.bis.org/publ/bcbs295.htm
    name: Net Stable Funding Ratio (Oct 2014)
  - type: Vocabulary
    url: vocabulary/basel-iii-vocabulary.yaml
    name: Basel III Vocabulary
  - type: JSON-LD
    url: json-ld/basel-iii-context.jsonld
    name: Basel III JSON-LD Context
  - name: Governance
    type: Governance
    data:
      - name: Governing Body
        description: Basel Committee on Banking Supervision (BCBS) at the Bank for International Settlements (BIS).
      - name: Oversight
        description: Group of Central Bank Governors and Heads of Supervision (GHOS) endorses all BCBS reforms.
      - name: Implementation
        description: National regulators implement Basel standards through domestic legislation; EU via CRD/CRR, US via Federal Reserve rules.
      - name: Transitional Period
        description: Basel III final package (Basel IV) transitions run from 2023 to full implementation by January 2028.
      - name: Membership
        description: 45 member institutions (central banks and bank supervisory authorities) from 28 jurisdictions.
  - name: Key Standards
    type: Features
    data:
      - name: CET1 Capital Ratio
        description: Common Equity Tier 1 capital ratio minimum of 4.5% of risk-weighted assets.
      - name: Tier 1 Capital Ratio
        description: Minimum Tier 1 capital ratio of 6% of risk-weighted assets.
      - name: Total Capital Ratio
        description: Minimum total capital ratio of 8% including Tier 2 capital instruments.
      - name: Capital Conservation Buffer
        description: Additional 2.5% CET1 buffer above minimum to absorb losses in stress periods.
      - name: Countercyclical Capital Buffer
        description: Variable buffer (0–2.5%) set by national authorities to dampen credit cycles.
      - name: G-SIB Surcharge
        description: Additional capital surcharge for Global Systemically Important Banks (1–3.5%).
      - name: Liquidity Coverage Ratio (LCR)
        description: 30-day liquidity stress test requiring sufficient High-Quality Liquid Assets (HQLA).
      - name: Net Stable Funding Ratio (NSFR)
        description: One-year structural funding stability requirement to limit maturity mismatch.
      - name: Leverage Ratio
        description: Non-risk-based Tier 1 capital backstop of at least 3% of total exposures.
      - name: Output Floor (Basel IV)
        description: Floor on internal model RWA outputs at 72.5% of standardized approach results.
      - name: FRTB Market Risk
        description: Fundamental Review of the Trading Book replaces Basel 2.5 market risk rules.
      - name: SA-CCR Credit Risk
        description: Standardized Approach for Counterparty Credit Risk replacing CEM and SM methods.
  - name: RegTech Use Cases
    type: UseCases
    data:
      - name: Capital Ratio Reporting
        description: Automated COREP capital ratio calculation and regulatory submission.
      - name: RWA Calculation
        description: Credit, market, and operational risk-weighted asset computation under standardized or IRB approaches.
      - name: LCR Monitoring
        description: Daily liquidity coverage ratio calculation and stress scenario modeling.
      - name: NSFR Compliance
        description: Net Stable Funding Ratio computation tracking available vs. required stable funding.
      - name: Leverage Ratio Computation
        description: Tier 1 capital over total exposure measure including off-balance-sheet items.
      - name: Stress Testing
        description: CCAR, EBA stress test scenario modeling for capital adequacy projections.
      - name: ICAAP Support
        description: Internal Capital Adequacy Assessment Process tooling and documentation.
      - name: FRTB Implementation
        description: Trading book boundary enforcement, sensitivities-based method, and IMA implementation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
