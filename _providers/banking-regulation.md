---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banking-regulation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/
- group: company
  title: ''
  type: Website
  url: https://www.fsb.org/
- group: company
  title: ''
  type: Website
  url: https://www.federalreserve.gov/supervisionreg.htm
- group: company
  title: ''
  type: Website
  url: https://www.eba.europa.eu/
- group: company
  title: ''
  type: Website
  url: https://www.ffiec.gov/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/banking-regulation-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/banking-regulation-context.jsonld
created: '2025-01-01'
description: Banking regulation encompasses the rules, standards, and frameworks governing banks and financial institutions. Key frameworks include the Basel Accords (Basel I, II, III, IV) for capital adequacy, the Dodd-Frank Act in the US, PSD2 and CRD IV/V in Europe, and anti-money laundering (AML) / know-your-customer (KYC) requirements. Regulatory technology (RegTech) APIs and data services help financial institutions automate compliance reporting, risk management, and supervisory data submissions.
features:
- description: APIs and platforms for Basel III risk-weighted asset and capital ratio calculations.
  name: Capital Adequacy Reporting
- description: Real-time transaction screening and suspicious activity reporting.
  name: AML Transaction Monitoring
- description: Identity verification, sanctions screening, and beneficial ownership APIs.
  name: KYC Onboarding
- description: Automated generation of supervisory reports (FINREP, COREP, FR Y-9C).
  name: Regulatory Reporting
- description: Scenario analysis and stress testing platforms for regulatory capital requirements.
  name: Stress Testing
- description: Data lineage, audit trails, and regulatory change management solutions.
  name: Compliance Data Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/banking-regulation.png
json_schemas:
- name: RegulatoryReport
  property_count: 8
  slug: regulatory-report
jsonld:
- class_count: 3
  name: Banking Regulation Context
  property_count: 13
  slug: banking-regulation-context
layout: provider
modified: '2026-04-21'
name: Banking Regulation
nav: Providers
network: true
overview: 'Banking Regulation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AML, Banking, Banking Regulation, Basel, and Compliance.


  The Banking Regulation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 9
rules:
- effective_rule_count: 5
  extends: []
  name: Banking Regulation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: banking-regulation-jsonschema-spectral-rules
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 43.3
    catalog_earned_first_party: 0.0
    catalog_gap: 71.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banking-regulation/refs/heads/main/screenshots/banking-regulation-2026-06-20T172952.png
security:
- kind: domain-security
  name: Banking Regulation Domain Security
  slug: banking-regulation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banking-regulation
tags:
- AML
- Banking
- Banking Regulation
- Basel
- Compliance
- Finance
- KYC
- RegTech
use_cases:
- description: International capital adequacy, leverage, and liquidity standards for banks.
  name: Basel III / IV
- description: US financial reform legislation covering derivatives, systemic risk, and consumer protection.
  name: Dodd-Frank Act
- description: EU Payment Services Directive 2 governing open banking and payment security.
  name: PSD2
- description: EU Capital Requirements Directive for bank capital, liquidity, and governance.
  name: CRD IV / V
- description: Anti-Money Laundering and Bank Secrecy Act compliance and reporting requirements.
  name: AML / BSA
- description: Know Your Customer identity verification and due diligence requirements.
  name: KYC
- description: Digital Operational Resilience Act for ICT risk in EU financial services.
  name: DORA
- description: US Comprehensive Capital Analysis and Review stress testing requirements.
  name: CCAR / DFAST
- description: Fundamental Review of the Trading Book market risk capital requirements.
  name: FRTB
website: https://www.bis.org/
---
