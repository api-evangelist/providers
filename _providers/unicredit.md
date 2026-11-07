---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API catalog for UniCredit developers
  name: UniCredit API
  slug: unicredit-api
- description: The Hydrogen API from UniCredit — 2 operation(s) for hydrogen.
  name: UniCredit Hydrogen API
  slug: unicredit-hydrogen-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/unicredit/llms/unicredit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unicredit-llms.txt
- group: design
  href: https://artifacts.apis.io/unicredit/rules/unicredit-rules.yml
  title: ''
  type: Spectral
  url: rules/unicredit-rules.yml
- group: design
  href: https://artifacts.apis.io/unicredit/json-ld/unicredit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unicredit-context.jsonld
- group: design
  href: https://artifacts.apis.io/unicredit/vocabulary/unicredit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unicredit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/unicredit/data-model/unicredit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unicredit-data-model.yml
- group: auth
  href: https://artifacts.apis.io/unicredit/authentication/unicredit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unicredit-authentication.yml
- group: design
  href: https://artifacts.apis.io/unicredit/conformance/unicredit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unicredit-conformance.yml
- group: other
  href: https://artifacts.apis.io/unicredit/hosts/unicredit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unicredit-hosts.yml
- group: other
  href: https://artifacts.apis.io/unicredit/vendors/unicredit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unicredit-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unicreditgroup.eu/en/info/privacy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.unicredit.eu/support/getting-started-public
- group: docs
  title: ''
  type: Documentation
  url: https://developer.unicredit.eu/
- group: auth
  href: https://artifacts.apis.io/unicredit/security/unicredit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unicredit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unicredit.eu
coverage:
  checked: '2026-10-15'
  detail: Developer portal provides only HTML pages without OpenAPI or other machine-readable contracts.
  evidence:
  - status: 0
    url: https://api.unicredit.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: UniCredit is a leading European banking group offering a full range of financial services, including corporate and investment banking, retail banking, asset management, and digital solutions. With a strong presence across Europe and a focus on innovation, UniCredit serves corporate clients, SMEs, and private customers, providing tailored financing, payment services, and advisory. The group emphasizes sustainability, digital transformation, and customer-centric approaches, operating in over 20 countries with a robust network of branches and digital channels.
json_schemas:
- name: GetHydrogenV1AccountsAccountidResponse
  property_count: 1
  slug: unicredit-get-hydrogen-v1-accounts-accountid-response
- name: GetHydrogenV1AccountsAccountidTransactionsResponse
  property_count: 2
  slug: unicredit-get-hydrogen-v1-accounts-accountid-transactions-response
jsonld:
- class_count: 2
  name: Unicredit Context
  property_count: 3
  slug: unicredit-context
layout: provider
modified: '2026-10-14'
name: UniCredit
nav: Providers
network: true
overview: 'UniCredit is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Hydrogen API, and 1 more. Tagged areas include Company, Banking, Financial Services, Europe, and Corporate Banking.


  The UniCredit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UniCredit''s developer surface includes authentication, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: UniCredit API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: unicredit-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 14.3
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 22.6
    discoverability: 60.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 25.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/unicredit/unicredit-2026-11-03T145424.png
security:
- kind: authentication
  name: Unicredit Authentication
  slug: unicredit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unicredit Domain Security
  slug: unicredit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: unicredit
tags:
- Company
- Banking
- Financial Services
- Europe
- Corporate Banking
website: https://www.unicredit.eu
---
