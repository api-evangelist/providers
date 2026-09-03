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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basel-iii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/bcbs/basel3.htm
- group: company
  title: ''
  type: Website
  url: https://www.eba.europa.eu/regulation-and-policy/own-funds-and-eligible-liabilities
- group: company
  title: ''
  type: Website
  url: https://www.federalreserve.gov/supervisionreg/Basel.htm
- group: company
  title: ''
  type: Website
  url: https://www.pra.boe.co.uk/pages/policy/crr
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/bcbs/publ/d424.htm
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/publ/bcbs189.htm
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/publ/bcbs238.htm
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/publ/bcbs295.htm
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/basel-iii-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/basel-iii-context.jsonld
- group: other
  title: ''
  type: Governance
  url: ''
created: '2025-01-01'
description: Basel III is a comprehensive global regulatory framework developed by the Basel Committee on Banking Supervision (BCBS) in response to the 2007-2008 financial crisis. It strengthens bank capital requirements by requiring higher quality and quantity of capital (CET1, Tier 1, Total Capital), introduces new liquidity standards (LCR and NSFR), adds a leverage ratio backstop, and includes countercyclical capital buffers and G-SIB surcharges. Basel III implementation in the EU/UK is delivered via CRD IV/V and CRR regulations. The final Basel III package (sometimes called Basel IV) addresses output floor and credit risk model constraints introduced in 2017.
examples:
- key_count: 15
  name: Basel Iii Capital Requirements Example
  slug: basel-iii-capital-requirements-example
features:
- description: Common Equity Tier 1 capital ratio minimum of 4.5% of risk-weighted assets.
  name: CET1 Capital Ratio
- description: Minimum Tier 1 capital ratio of 6% of risk-weighted assets.
  name: Tier 1 Capital Ratio
- description: Minimum total capital ratio of 8% including Tier 2 capital instruments.
  name: Total Capital Ratio
- description: Additional 2.5% CET1 buffer above minimum to absorb losses in stress periods.
  name: Capital Conservation Buffer
- description: Variable buffer (0–2.5%) set by national authorities to dampen credit cycles.
  name: Countercyclical Capital Buffer
- description: Additional capital surcharge for Global Systemically Important Banks (1–3.5%).
  name: G-SIB Surcharge
- description: 30-day liquidity stress test requiring sufficient High-Quality Liquid Assets (HQLA).
  name: Liquidity Coverage Ratio (LCR)
- description: One-year structural funding stability requirement to limit maturity mismatch.
  name: Net Stable Funding Ratio (NSFR)
- description: Non-risk-based Tier 1 capital backstop of at least 3% of total exposures.
  name: Leverage Ratio
- description: Floor on internal model RWA outputs at 72.5% of standardized approach results.
  name: Output Floor (Basel IV)
- description: Fundamental Review of the Trading Book replaces Basel 2.5 market risk rules.
  name: FRTB Market Risk
- description: Standardized Approach for Counterparty Credit Risk replacing CEM and SM methods.
  name: SA-CCR Credit Risk
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basel-iii.png
jsonld:
- class_count: 0
  name: Basel Iii Context
  property_count: 15
  slug: basel-iii-context
layout: provider
modified: '2026-04-21'
name: Basel III
nav: Providers
network: true
overview: 'Basel III is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking Regulation, Basel III, Capital Adequacy, Capital Requirements, and Compliance.


  The Basel III catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 18
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 15.2
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basel-iii/refs/heads/main/screenshots/basel-iii-2026-06-20T173017.png
security:
- kind: domain-security
  name: Basel Iii Domain Security
  slug: basel-iii-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: basel-iii
tags:
- Banking Regulation
- Basel III
- Capital Adequacy
- Capital Requirements
- Compliance
- Finance
- Liquidity
- Risk Management
use_cases:
- description: Automated COREP capital ratio calculation and regulatory submission.
  name: Capital Ratio Reporting
- description: Credit, market, and operational risk-weighted asset computation under standardized or IRB approaches.
  name: RWA Calculation
- description: Daily liquidity coverage ratio calculation and stress scenario modeling.
  name: LCR Monitoring
- description: Net Stable Funding Ratio computation tracking available vs. required stable funding.
  name: NSFR Compliance
- description: Tier 1 capital over total exposure measure including off-balance-sheet items.
  name: Leverage Ratio Computation
- description: CCAR, EBA stress test scenario modeling for capital adequacy projections.
  name: Stress Testing
- description: Internal Capital Adequacy Assessment Process tooling and documentation.
  name: ICAAP Support
- description: Trading book boundary enforcement, sensitivities-based method, and IMA implementation.
  name: FRTB Implementation
website: https://www.bis.org/bcbs/basel3.htm
---
