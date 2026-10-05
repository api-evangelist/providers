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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: JSON-based "A-REST" API for SUSE Manager (SUMA), used to manage systems, channels, configuration, errata, and users across Linux infrastructure. Calls use GET for retrievals, POST for changes, and POS
  name: SUSE Manager API
  slug: suma-api
- description: REST API for SUSE Rancher Prime Kubernetes management platform, used to manage clusters, projects, workloads, users, and policies. Supports v3 API endpoints with bearer token authentication.
  name: SUSE Rancher API
  slug: rancher-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/authentication/suse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/suse-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/llms/suse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/suse-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/well-known/suse-suse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/suse-suse-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/well-known/suse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/suse-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/well-known/suse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/suse-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/hosts/suse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/vendors/suse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suse-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/packages/suse-packages.yml
  title: ''
  type: SDKs
  url: packages/suse-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/packages/suse-packages.yml
  title: ''
  type: Packages
  url: packages/suse-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suse.com/company/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.suse.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.suse.com/
- group: auth
  title: ''
  type: Security
  url: https://www.suse.com/support/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.suse.com/news/
- group: start
  title: ''
  type: Login
  url: https://www.suse.com/saml2/login/?returnUrl=https%3a%2f%2fwww.suse.com%2f
- group: other
  title: ''
  type: Leadership
  url: https://www.suse.com/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.suse.com/appliance/kiwi-9/html/kiwi/quick-start.html
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.suse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SUSE
- group: company
  title: ''
  type: Website
  url: https://suse.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/security/suse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/suse-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/security/suse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suse-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.suse.com/c/feed/
coverage:
  checked: '2026-10-03'
  detail: API endpoints return 401 Unauthorized, indicating authentication required.
  evidence:
  - status: 401
    url: https://api.suse.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-05-11'
description: SUSE is a global provider of open source enterprise solutions, offering SUSE Linux Enterprise Server, SUSE Rancher Prime, SUSE Manager, SUSE Edge, and AI Factory. Its products expose REST and A-REST APIs for automation, configuration, and integration across Linux, Kubernetes, edge, and AI workloads. Documentation and developer portals provide comprehensive guides, reference, and SDKs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suse.png
layout: provider
modified: '2026-09-16'
name: SUSE
nav: Providers
network: true
overview: 'SUSE publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Linux, Kubernetes, Enterprise Linux, Systems Management, and Open Source.


  SUSE''s developer surface includes authentication, support, getting-started guide, documentation, engineering blog, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.7
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 76.8
    operational_transparency: 31.6
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/screenshots/suse-2026-06-20T194741.png
security:
- kind: authentication
  name: Suse Authentication
  slug: suse-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Suse Domain Security
  slug: suse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Suse Vulnerability Disclosure
  slug: suse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: suse
tags:
- Linux
- Kubernetes
- Enterprise Linux
- Systems Management
- Open Source
- Container Management
website: https://suse.com
---
