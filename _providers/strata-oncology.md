---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Strata Oncology website at strataoncology.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: Strata Oncology Website (WordPress REST)
  slug: strataoncology-com-website-wordpress-rest
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/strata-oncology/mcp/strata-oncology-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/strata-oncology-mcp.yml
- group: other
  href: https://artifacts.apis.io/strata-oncology/overlays/strata-oncology-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strata-oncology-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://strataoncology.com/
- group: company
  title: ''
  type: About
  url: https://strataoncology.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://strataoncology.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://strataoncology.com/news-and-publications/
- group: company
  title: ''
  type: BlogRSS
  url: https://strataoncology.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://strataoncology.com/create-account/
- group: start
  title: ''
  type: Login
  url: https://portal.strataoncology.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strataoncology.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strataoncology.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://strataoncology.com/privacy-practices/
- group: other
  title: ''
  type: NoSurprisesAct
  url: https://strataoncology.com/no-surprises-act/
- group: commercial
  title: ''
  type: Billing
  url: https://strataoncology.com/resources/patient-billing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StrataOncology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/strata-oncology/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StrataOncology
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/strata-oncology_stock/
- group: design
  href: https://artifacts.apis.io/strata-oncology/conventions/strata-oncology-conventions.yml
  title: ''
  type: Conventions
  url: conventions/strata-oncology-conventions.yml
- group: design
  href: https://artifacts.apis.io/strata-oncology/conformance/strata-oncology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/strata-oncology-conformance.yml
- group: design
  href: https://artifacts.apis.io/strata-oncology/lifecycle/strata-oncology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/strata-oncology-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/strata-oncology/packages/strata-oncology-packages.yml
  title: ''
  type: Packages
  url: packages/strata-oncology-packages.yml
- group: agent
  href: https://artifacts.apis.io/strata-oncology/llms/strata-oncology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strata-oncology-llms.txt
- group: agent
  href: https://artifacts.apis.io/strata-oncology/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/strata-oncology/security/strata-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strata-oncology-domain-security.yml
- group: design
  href: https://artifacts.apis.io/strata-oncology/errors/strata-oncology-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/strata-oncology-problem-types.yml
- group: design
  href: https://artifacts.apis.io/strata-oncology/data-model/strata-oncology-data-model.yml
  title: ''
  type: DataModel
  url: data-model/strata-oncology-data-model.yml
created: '2026-08-02'
description: Strata Oncology is a precision oncology company founded in 2015 by Dan Rhodes and Scott Tomlins and headquartered in Ann Arbor, Michigan. It develops and runs predictive biomarker tests out of its own high-throughput CLIA laboratory, including StrataNGS tumor genomic profiling, the Immunotherapy Response Score for anti-PD-1/PD-L1 monotherapy benefit, PD-L1 IHC testing, and Antibody-Drug Conjugate Treatment Response Scores. Testing is delivered to health systems through the Strata Precision Oncology Network, with ordering and results handled through the login-gated Strata Request Portal and the Strata Assistant app distributed in the Epic App Orchard. Strata Oncology publishes no public developer program or API documentation; the only anonymous machine-readable surface API Evangelist could verify is the WordPress REST content API behind strataoncology.com.
image: https://strataoncology.com/wp-content/uploads/2022/09/Strata-Oncology-Logo_Symbol-Dark-Theme.svg
layout: provider
modified: '2026-08-02'
name: Strata Oncology
nav: Providers
network: true
overview: 'Strata Oncology is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Precision Medicine, Oncology, and Genomics.


  Strata Oncology''s developer surface includes engineering blog, signup flow, and 25 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 8.9
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 20.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/strata-oncology/strata-oncology-2026-09-02T160950.png
security:
- kind: authentication
  name: Strata Oncology Authentication
  slug: strata-oncology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Strata Oncology Domain Security
  slug: strata-oncology-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: Assemble a Strata Oncology company profile
  slug: strata-oncology-company-profile
- name: Track Strata Oncology publications and press releases
  slug: strata-oncology-track-publications
slug: strata-oncology
tags:
- Company
- Healthcare
- Precision Medicine
- Oncology
- Genomics
- Diagnostics
- Laboratory
- Life Sciences
- Biomarkers
- Clinical Trials
website: https://strataoncology.com/
---
