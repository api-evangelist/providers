---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The domain API from Cyble — 8 operation(s) for domain.
  name: Cyble Domain API
  slug: cyble-domain-api
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The ExposedBuckets API from Cyble — 3 operation(s) for exposedbuckets.
  name: Cyble Exposed Buckets API
  slug: cyble-exposedbuckets-api
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The ExposedFiles API from Cyble — 3 operation(s) for exposedfiles.
  name: Cyble Exposed Files API
  slug: cyble-exposedfiles-api
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The Fields API from Cyble — 3 operation(s) for fields.
  name: Cyble Fields API
  slug: cyble-fields-api
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The Health API from Cyble — 1 operation(s) for health.
  name: Cyble Health API
  slug: cyble-health-api
- baseURL: https://api.odin.io/
  baseurl_source: declared
  description: The Hosts API from Cyble — 9 operation(s) for hosts.
  name: Cyble Hosts API
  slug: cyble-hosts-api
artifact_total: 17
collections:
- collection_type: open
  name: Odin
  slug: open-cyble-odin
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://cyble.com/feed/
- group: other
  href: https://artifacts.apis.io/cyble/capabilities/cyble-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cyble-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/cyble/security/cyble-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cyble-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://cyble.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.odin.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.odin.io/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.odin.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.odin.io/authentication
- group: operate
  title: ''
  type: Support
  url: https://search.odin.io/community
- group: company
  title: ''
  type: Blog
  url: https://cyble.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cybledev
- group: commercial
  title: ''
  type: Pricing
  url: https://search.odin.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://search.odin.io/login
- group: start
  title: ''
  type: Login
  url: https://search.odin.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://search.odin.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://search.odin.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cybleai/cyble-odin-public/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.odin.io
- group: auth
  title: ''
  type: Security
  url: https://cyble.com/security-disclosure-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cyble.com/
- group: auth
  href: https://artifacts.apis.io/cyble/well-known/cyble-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cyble-security.txt
- group: agent
  href: https://artifacts.apis.io/cyble/well-known/cyble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyble-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyble/a2a/cyble-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cyble-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cyble/llms/cyble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyble-llms.txt
- group: build
  href: https://artifacts.apis.io/cyble/packages/cyble-packages.yml
  title: ''
  type: Packages
  url: packages/cyble-packages.yml
- group: build
  href: https://artifacts.apis.io/cyble/packages/cyble-packages.yml
  title: ''
  type: SDKs
  url: packages/cyble-packages.yml
- group: build
  href: https://artifacts.apis.io/cyble/cli/cyble-cli.yml
  title: ''
  type: CLI
  url: cli/cyble-cli.yml
- group: auth
  href: https://artifacts.apis.io/cyble/authentication/cyble-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cyble-authentication.yml
- group: design
  href: https://artifacts.apis.io/cyble/conventions/cyble-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cyble-conventions.yml
- group: design
  href: https://artifacts.apis.io/cyble/errors/cyble-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cyble-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cyble/lifecycle/cyble-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cyble-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cyble/conformance/cyble-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyble-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cyble/security/cyble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyble-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cyble/security/cyble-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyble-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cyble/data-model/cyble-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cyble-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cyble/rate-limits/cyble-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cyble-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cyble/plans/cyble-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cyble-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cyble/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/cyble/overlays/cyble-odin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cyble-odin-overlay.yaml
created: '2026-08-11'
description: 'Cyble Inc. is an AI-native cyber threat intelligence company headquartered in Cupertino, California, serving enterprises, governments and federal bodies with dark-web monitoring, attack-surface management and actionable threat intelligence. Its product family includes Cyble Vision (the enterprise threat-intelligence platform, integrated with 70+ SIEM/SOAR/TIP platforms), Cyble Hawk (built for federal and government bodies), AmIBreached (dark-web exposure monitoring), The Cyber Express (its security news publication), and ODIN — a public internet-scanning search engine that indexes 254M+ IPv4 hosts, 3B+ services across 500+ ports, 789k+ exposed cloud storage buckets, 117B+ exposed files and 10B+ subdomains. ODIN is the company''s public, self-serve developer surface: a documented REST API at api.odin.io with a published OpenAPI 3.0.1 definition, first-party Go/Python/JavaScript SDKs, a Go CLI, a public Postman collection, and an llms.txt documentation index.'
finops:
- has_sources: true
  method: derived
  name: Cyble Finops
  primary_unit: ''
  service_category: ''
  slug: cyble-finops
  template: true
image: https://search.odin.io/opengraph-image.png
layout: provider
modified: '2026-10-06'
name: Cyble
nav: Providers
network: true
overview: 'Cyble publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domain API, Exposed Buckets API, Exposed Files API, and 3 more. Tagged areas include Threat Intelligence, Cybersecurity, Attack Surface Management, Internet Scanning, and Dark Web Monitoring.


  Cyble''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Cyble Plans Pricing
  plan_count: 0
  slug: cyble-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Cyble Rate Limits
  slug: cyble-rate-limits
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 48.0
    developer_ergonomics: 78.0
    discoverability: 66.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cyble/cyble-2026-08-17T080843.png
security:
- kind: authentication
  name: Cyble Authentication
  slug: cyble-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cyble Domain Security
  slug: cyble-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cyble Vulnerability Disclosure
  slug: cyble-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cyble Trust Center
  slug: cyble-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: ODIN attack-surface sweep for a domain
  slug: cyble-odin-attack-surface-sweep
- name: ODIN CVE exposure check across an IP range or ASN
  slug: cyble-odin-cve-exposure-check
- name: ODIN exposed bucket and file hunt
  slug: cyble-odin-exposed-data-hunt
slug: cyble
tags:
- Threat Intelligence
- Cybersecurity
- Attack Surface Management
- Internet Scanning
- Dark Web Monitoring
- Vulnerability Management
- CVE
- ExposedBuckets
- Domain Intelligence
- WHOIS
- OSINT
- Security
- A2A
website: https://cyble.com/
---
