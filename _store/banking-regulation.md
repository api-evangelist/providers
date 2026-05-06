---
aid: banking-regulation
name: Banking Regulation
description: Banking regulation encompasses the rules, standards, and frameworks governing banks and financial institutions. Key frameworks include the Basel Accords (Basel I, II, III, IV) for capital adequacy, the Dodd-Frank Act in the US, PSD2 and CRD IV/V in Europe, and anti-money laundering (AML) / know-your-customer (KYC) requirements. Regulatory technology (RegTech) APIs and data services help financial institutions automate compliance reporting, risk management, and supervisory data submissions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AML
  - Banking
  - Banking Regulation
  - Basel
  - Compliance
  - Finance
  - KYC
  - RegTech
url: https://raw.githubusercontent.com/api-evangelist/banking-regulation/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.bis.org/
    name: Bank for International Settlements
  - type: Website
    url: https://www.fsb.org/
    name: Financial Stability Board
  - type: Website
    url: https://www.federalreserve.gov/supervisionreg.htm
    name: Federal Reserve Supervision & Regulation
  - type: Website
    url: https://www.eba.europa.eu/
    name: European Banking Authority
  - type: Website
    url: https://www.ffiec.gov/
    name: Federal Financial Institutions Examination Council
  - type: Vocabulary
    url: vocabulary/banking-regulation-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/banking-regulation-context.jsonld
  - name: Key Frameworks
    type: UseCases
    data:
      - name: Basel III / IV
        description: International capital adequacy, leverage, and liquidity standards for banks.
      - name: Dodd-Frank Act
        description: US financial reform legislation covering derivatives, systemic risk, and consumer protection.
      - name: PSD2
        description: EU Payment Services Directive 2 governing open banking and payment security.
      - name: CRD IV / V
        description: EU Capital Requirements Directive for bank capital, liquidity, and governance.
      - name: AML / BSA
        description: Anti-Money Laundering and Bank Secrecy Act compliance and reporting requirements.
      - name: KYC
        description: Know Your Customer identity verification and due diligence requirements.
      - name: DORA
        description: Digital Operational Resilience Act for ICT risk in EU financial services.
      - name: CCAR / DFAST
        description: US Comprehensive Capital Analysis and Review stress testing requirements.
      - name: FRTB
        description: Fundamental Review of the Trading Book market risk capital requirements.
  - name: RegTech Categories
    type: Features
    data:
      - name: Capital Adequacy Reporting
        description: APIs and platforms for Basel III risk-weighted asset and capital ratio calculations.
      - name: AML Transaction Monitoring
        description: Real-time transaction screening and suspicious activity reporting.
      - name: KYC Onboarding
        description: Identity verification, sanctions screening, and beneficial ownership APIs.
      - name: Regulatory Reporting
        description: Automated generation of supervisory reports (FINREP, COREP, FR Y-9C).
      - name: Stress Testing
        description: Scenario analysis and stress testing platforms for regulatory capital requirements.
      - name: Compliance Data Management
        description: Data lineage, audit trails, and regulatory change management solutions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
