---
aid: basel-compliance
name: Basel Compliance
description: Basel Compliance covers the regulatory frameworks and technical standards issued by the Basel Committee on Banking Supervision (BCBS) at the Bank for International Settlements. The Basel Accords establish minimum capital adequacy, leverage, liquidity, and risk management requirements for internationally active banks. RegTech platforms provide APIs to automate Basel compliance calculations, reporting (COREP, FINREP), and supervisory submissions.
type: Index
x-type: topic
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking Regulation
  - Basel
  - Capital Adequacy
  - Compliance
  - Finance
  - Risk Management
  - RegTech
url: https://raw.githubusercontent.com/api-evangelist/basel-compliance/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.bis.org/bcbs/
    name: Basel Committee on Banking Supervision
  - type: Website
    url: https://www.bis.org/bcbs/basel3.htm
    name: Basel III Framework
  - type: Website
    url: https://www.eba.europa.eu/
    name: European Banking Authority
  - type: Website
    url: https://www.federalreserve.gov/supervisionreg/Basel.htm
    name: Federal Reserve - Basel Implementation
  - type: Website
    url: https://www.bis.org/bcbs/publ/d424.htm
    name: BCBS Basel III Finalising Post-Crisis Reforms (Dec 2017)
  - type: Website
    url: https://www.eba.europa.eu/regulation-and-policy/supervisory-reporting
    name: EBA COREP/FINREP Reporting Framework
  - type: Vocabulary
    url: vocabulary/basel-compliance-vocabulary.yaml
    name: Basel Compliance Vocabulary
  - type: JSON-LD
    url: json-ld/basel-compliance-context.jsonld
    name: Basel Compliance JSON-LD Context
  - name: Data Providers
    type: DataProviders
    data:
      - name: BIS Statistics
        url: https://stats.bis.org/
        description: Bank for International Settlements statistical data on global banking metrics.
      - name: EBA Data
        url: https://www.eba.europa.eu/risk-analysis-and-data
        description: European Banking Authority risk analysis data and supervisory reporting datasets.
      - name: Federal Reserve Statistical Release
        url: https://www.federalreserve.gov/releases/
        description: US Federal Reserve statistical releases covering bank capital ratios and liquidity.
      - name: S&P Global Market Intelligence
        url: https://www.spglobal.com/marketintelligence/en/
        description: Commercial provider of bank regulatory capital and balance sheet data.
      - name: Axiom SL / SS&C
        url: https://www.ssctech.com/solutions/axiom-sl
        description: RegTech platform for COREP, FINREP, and Basel regulatory reporting automation.
      - name: Moody's Analytics
        url: https://www.moodysanalytics.com/
        description: Risk and compliance solutions for capital calculation, ICAAP, and stress testing.
  - name: Key Standards
    type: Features
    data:
      - name: Pillar 1 - Minimum Capital Requirements
        description: Capital requirements for credit risk, market risk, and operational risk.
      - name: Pillar 2 - Supervisory Review
        description: Internal capital adequacy assessment process (ICAAP) and supervisory evaluation (SREP).
      - name: Pillar 3 - Market Discipline
        description: Disclosure requirements for risk exposures and capital adequacy.
      - name: LCR - Liquidity Coverage Ratio
        description: Short-term liquidity stress test requiring sufficient high-quality liquid assets.
      - name: NSFR - Net Stable Funding Ratio
        description: Long-term funding stability requirement relative to asset composition.
      - name: Leverage Ratio
        description: Non-risk-based backstop capital measure limiting excessive leverage.
      - name: FRTB - Market Risk
        description: Fundamental Review of the Trading Book capital requirements for market risk.
      - name: COREP Reporting
        description: EU common reporting framework for capital adequacy and large exposures.
      - name: Output Floor (Basel IV)
        description: Requires internal model RWA to be at least 72.5% of standardized approach results.
  - name: RegTech Use Cases
    type: UseCases
    data:
      - name: Capital Ratio Calculation
        description: Automated CET1, Tier 1, and Total Capital ratio calculations.
      - name: Risk-Weighted Asset Computation
        description: Standardized and IRB approach RWA calculations for credit risk.
      - name: Liquidity Reporting
        description: Automated LCR and NSFR calculation and regulatory reporting.
      - name: COREP/FINREP Submission
        description: Automated generation of supervisory reports for regulators.
      - name: Stress Testing
        description: Capital adequacy stress testing under regulatory scenarios (CCAR, EBA).
      - name: Large Exposure Monitoring
        description: Track and report exposures exceeding regulatory thresholds.
      - name: ICAAP Documentation
        description: Internal capital adequacy documentation and SREP preparation support.
  - name: Integrations
    type: Integrations
    data:
      - name: Axiom SL
      - name: Moody's Analytics RiskConfidence
      - name: Oracle Financial Services
      - name: SAS Risk Management
      - name: Wolters Kluwer OneSumX
      - name: FIS Regulatory Reporting
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
