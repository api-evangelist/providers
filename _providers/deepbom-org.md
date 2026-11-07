---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for DeepBOM CLI and platform
  name: DeepBOM API
  slug: deepbom-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/deepbom-org/cli/deepbom-org-cli.yml
  title: ''
  type: CLI
  url: cli/deepbom-org-cli.yml
- group: agent
  href: https://artifacts.apis.io/deepbom-org/llms/deepbom-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepbom-org-llms.txt
- group: other
  href: https://artifacts.apis.io/deepbom-org/hosts/deepbom-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepbom-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepbom-org/vendors/deepbom-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepbom-org-vendors.yml
- group: build
  href: https://artifacts.apis.io/deepbom-org/packages/deepbom-org-packages.yml
  title: ''
  type: SDKs
  url: packages/deepbom-org-packages.yml
- group: build
  href: https://artifacts.apis.io/deepbom-org/packages/deepbom-org-packages.yml
  title: ''
  type: Packages
  url: packages/deepbom-org-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepbom.org/terms
- group: operate
  title: ''
  type: Support
  url: https://deepbom.org/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepbom.org/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://deepbom.org/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://deepbom.org/guides/cli/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://deepbom.org/get-started/
- group: auth
  href: https://artifacts.apis.io/deepbom-org/security/deepbom-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepbom-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepbom.org/
coverage:
  checked: '2026-11-05'
  detail: Documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 404
    url: https://deepbom.org/openapi.json
  - status: 404
    url: https://api.deepbom.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DEEPBOM provides tools to inspect AI deployment artifacts locally, reviewing model structure, quantization, and changes. It enables export of hash‑bound evidence for deployment decisions, helping developers ensure safe and compliant AI model deployment.
image: https://deepbom.org/web/og-image.png
layout: provider
modified: '2026-11-05'
name: DEEPBOM
nav: Providers
network: true
overview: 'DEEPBOM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Model Inspection, Deployment, Security, and Open Source.


  DEEPBOM''s developer surface includes CLI, support, documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepbom Org Domain Security
  slug: deepbom-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: deepbom-org
tags:
- Artificial Intelligence
- Model Inspection
- Deployment
- Security
- Open Source
- Company
website: https://deepbom.org/
---
