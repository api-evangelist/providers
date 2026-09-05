---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Keygen Agentic Access
  operation_count: 63
  slug: keygen-agentic-access
  summary_line: 63 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Binary artifacts attached to releases.
  name: Keygen Artifacts API
  slug: keygen-artifacts-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Hardware components of a machine fingerprint.
  name: Keygen Components API
  slug: keygen-components-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Named feature flags attached to policies and licenses.
  name: Keygen Entitlements API
  slug: keygen-entitlements-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Issue, validate, and manage license keys.
  name: Keygen Licenses API
  slug: keygen-licenses-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Activate and manage node-locked machines.
  name: Keygen Machines API
  slug: keygen-machines-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Licensing rules that govern licenses.
  name: Keygen Policies API
  slug: keygen-policies-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Concurrent processes running on a machine.
  name: Keygen Processes API
  slug: keygen-processes-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Applications being licensed and distributed.
  name: Keygen Products API
  slug: keygen-products-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Distributable, semver-tagged releases.
  name: Keygen Releases API
  slug: keygen-releases-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Authenticate and manage bearer tokens.
  name: Keygen Tokens API
  slug: keygen-tokens-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: End users and license owners.
  name: Keygen Users API
  slug: keygen-users-api
- baseURL: https://api.keygen.sh/v1/accounts/{account}
  baseurl_source: declared
  description: Webhook endpoints and events.
  name: Keygen Webhooks API
  slug: keygen-webhooks-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Keygen Artifacts API
  slug: open-keygen-artifacts-api
- collection_type: open
  name: Keygen Artifacts Components API
  slug: open-keygen-components-api
- collection_type: open
  name: Keygen Artifacts Entitlements API
  slug: open-keygen-entitlements-api
- collection_type: open
  name: Keygen Artifacts Licenses API
  slug: open-keygen-licenses-api
- collection_type: open
  name: Keygen Artifacts Machines API
  slug: open-keygen-machines-api
- collection_type: open
  name: Keygen Artifacts Policies API
  slug: open-keygen-policies-api
- collection_type: open
  name: Keygen Artifacts Processes API
  slug: open-keygen-processes-api
- collection_type: open
  name: Keygen Artifacts Products API
  slug: open-keygen-products-api
- collection_type: open
  name: Keygen Artifacts Releases API
  slug: open-keygen-releases-api
- collection_type: open
  name: Keygen Artifacts Tokens API
  slug: open-keygen-tokens-api
- collection_type: open
  name: Keygen Artifacts Users API
  slug: open-keygen-users-api
- collection_type: open
  name: Keygen Artifacts Webhooks API
  slug: open-keygen-webhooks-api
- collection_type: open
  name: Keygen API
  slug: open-keygen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keygen-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/keygen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/keygen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keygen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keygen-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keygen-sh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keygen-sh
- group: company
  title: ''
  type: Website
  url: https://keygen.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://keygen.sh/docs/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/keygen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keygen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keygen-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://keygen.sh/blog/feed.xml
created: '2026-07-01'
description: Keygen is a software licensing, entitlements, and distribution API for desktop, on-prem, IoT, and other installed applications. It issues license keys, activates and tracks machines, enforces policy-based entitlements, and distributes releases and artifacts for auto-updates. Keygen ships as the source-available, self-hostable Keygen CE / EE and as the managed Keygen Cloud, exposing a JSON:API interface under api.keygen.sh.
finops:
- name: Keygen Finops
  service_category: Developer Tools
  slug: keygen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keygen.png
layout: provider
modified: '2026-07-01'
name: Keygen
nav: Providers
network: true
overview: 'Keygen publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Components API, Entitlements API, and 9 more. Tagged areas include Software Licensing, Entitlements, License Keys, Machine Activation, and Distribution.


  Keygen''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Keygen Plans Pricing
  plan_count: 5
  slug: keygen-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Keygen Rate Limits
  slug: keygen-rate-limits
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Keygen Authentication
  slug: keygen-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Keygen Domain Security
  slug: keygen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Keygen Vulnerability Disclosure
  slug: keygen-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Keygen Trust Center
  slug: keygen-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: keygen
tags:
- Software Licensing
- Entitlements
- License Keys
- Machine Activation
- Distribution
- Auto-Update
website: https://keygen.sh/
---
