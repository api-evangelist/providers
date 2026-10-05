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
    agent_skills: derived
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
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Hpe Agentic Access
  operation_count: 20
  slug: hpe-agentic-access
  summary_line: 20 operations · 14 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Unified REST API gateway for HPE GreenLake edge-to-cloud services including Compute Ops Management, Data Services Cloud Console, identity, workspaces, and API client credentials. Conforms to OpenAPI 3
  name: HPE GreenLake API
  slug: greenlake-api
- baseURL: https://global.api.greenlake.hpe.com
  baseurl_source: declared
  description: The Authorization API from Hewlett Packard Enterprise — 7 operation(s) for authorization.
  name: Hewlett Packard Enterprise Authorization API
  slug: hpe-authorization-api
- baseURL: https://global.api.greenlake.hpe.com
  baseurl_source: declared
  description: The Identity API from Hewlett Packard Enterprise — 2 operation(s) for identity.
  name: Hewlett Packard Enterprise Identity API
  slug: hpe-identity-api
- baseURL: https://global.api.greenlake.hpe.com
  baseurl_source: declared
  description: The Workspaces API from Hewlett Packard Enterprise — 3 operation(s) for workspaces.
  name: Hewlett Packard Enterprise Workspaces API
  slug: hpe-workspaces-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HPE GreenLake Authorization API
  slug: open-hpe-authorization-api
- collection_type: open
  name: HPE GreenLake Authorization Identity API
  slug: open-hpe-identity-api
- collection_type: open
  name: HPE GreenLake Authorization Workspaces API
  slug: open-hpe-workspaces-api
- collection_type: open
  name: HPE GreenLake API
  slug: open-hpe
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/rate-limits/hpe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hpe-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/rules/hpe-rules.yml
  title: ''
  type: Spectral
  url: rules/hpe-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/vocabulary/hpe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hpe-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/changelog/hpe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hpe-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/conventions/hpe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hpe-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/lifecycle/hpe-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hpe-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/lifecycle/hpe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hpe-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/conformance/hpe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hpe-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/llms/hpe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hpe-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/hosts/hpe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hpe-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/vendors/hpe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hpe-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.greenlake.hpe.com/docs/greenlake/services/compute-ops-mgmt/ahs/guide
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/capabilities/hpe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hpe-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/agentic-access/hpe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hpe-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/security/hpe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hpe-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/authentication/hpe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hpe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HewlettPackard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hewlett-packard-enterprise
- group: company
  title: ''
  type: Website
  url: https://www.hpe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.greenlake.hpe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hpe.com
- group: start
  title: ''
  type: Signup
  url: https://common.cloud.hpe.com/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HPE
coverage:
  checked: '2026-10-04'
  detail: Documentation pages are rendered via Redocly and the API host returns 403 for OpenAPI endpoints, preventing machine-readable spec retrieval.
  evidence:
  - status: 403
    url: https://global.api.greenlake.hpe.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-05-11'
description: Hewlett Packard Enterprise (HPE) is a global edge-to-cloud technology company providing servers, storage, networking, and hybrid cloud services, with HPE GreenLake serving as the unified edge-to-cloud platform delivering infrastructure as a service. The HPE GreenLake developer platform exposes OpenAPI 3.0 REST APIs covering compute, storage, networking, data services, identity, and workspace management, all authenticated via OAuth 2.0 client credentials and bearer tokens through a unified global API gateway.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hpe.png
layout: provider
modified: '2026-05-11'
name: Hewlett Packard Enterprise
nav: Providers
network: true
overview: 'Hewlett Packard Enterprise publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Identity API, Workspaces API, and 1 more. Tagged areas include Cloud, Edge to Cloud, Infrastructure-as-a-Service, Compute, and Storage.


  The Hewlett Packard Enterprise catalog on APIs.io includes 1 Spectral governance ruleset.


  Hewlett Packard Enterprise''s developer surface includes changelog, getting-started guide, authentication, documentation, signup flow, and 19 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 10
  name: Hpe Rate Limits
  slug: hpe-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Hewlett Packard Enterprise API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hpe-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.5
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 48.7
    developer_ergonomics: 44.6
    discoverability: 78.6
    operational_transparency: 57.9
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/screenshots/hpe-2026-06-20T182854.png
security:
- kind: authentication
  name: Hpe Authentication
  slug: hpe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hpe Domain Security
  slug: hpe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hpe
tags:
- Cloud
- Edge to Cloud
- Infrastructure-as-a-Service
- Compute
- Storage
- Networking
- Hybrid Cloud
- Enterprise IT
- Data Center
website: https://www.hpe.com
---
