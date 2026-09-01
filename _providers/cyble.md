---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The domain API from Cyble — 8 operation(s) for domain.
  name: Cyble Domain API
  slug: cyble-domain-api
- description: The ExposedBuckets API from Cyble — 3 operation(s) for exposedbuckets.
  name: Cyble Exposed Buckets API
  slug: cyble-exposedbuckets-api
- description: The ExposedFiles API from Cyble — 3 operation(s) for exposedfiles.
  name: Cyble Exposed Files API
  slug: cyble-exposedfiles-api
- description: The Fields API from Cyble — 3 operation(s) for fields.
  name: Cyble Fields API
  slug: cyble-fields-api
- description: The Health API from Cyble — 1 operation(s) for health.
  name: Cyble Health API
  slug: cyble-health-api
- description: The Hosts API from Cyble — 9 operation(s) for hosts.
  name: Cyble Hosts API
  slug: cyble-hosts-api
artifact_total: 13
collections:
- collection_type: open
  name: Odin
  slug: open-cyble-odin
common:
- group: auth
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
  title: ''
  type: SecurityTxt
  url: well-known/cyble-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cyble-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/cyble-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyble-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cyble-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cyble-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cyble-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyble-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cyble-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cyble-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyble-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyble-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyble-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyble-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cyble-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cyble-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cyble-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cyble-odin-overlay.yaml
created: '2026-08-11'
description: 'Cyble Inc. is an AI-native cyber threat intelligence company headquartered in Cupertino, California, serving enterprises, governments and federal bodies with dark-web monitoring, attack-surface management and actionable threat intelligence. Its product family includes Cyble Vision (the enterprise threat-intelligence platform, integrated with 70+ SIEM/SOAR/TIP platforms), Cyble Hawk (built for federal and government bodies), AmIBreached (dark-web exposure monitoring), The Cyber Express (its security news publication), and ODIN — a public internet-scanning search engine that indexes 254M+ IPv4 hosts, 3B+ services across 500+ ports, 789k+ exposed cloud storage buckets, 117B+ exposed files and 10B+ subdomains. ODIN is the company''s public, self-serve developer surface: a documented REST API at api.odin.io with a published OpenAPI 3.0.1 definition, first-party Go/Python/JavaScript SDKs, a Go CLI, a public Postman collection, and an llms.txt documentation index.'
image: https://search.odin.io/opengraph-image.png
layout: provider
modified: '2026-08-11'
name: Cyble
nav: Providers
network: true
overview: 'Cyble publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Domain API, Exposed Buckets API, Exposed Files API, and 3 more. Tagged areas include Threat Intelligence, Cybersecurity, Attack Surface Management, Internet Scanning, and Dark Web Monitoring.


  Cyble''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Cyble Plans Pricing
  plan_count: 0
  slug: cyble-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Cyble Rate Limits
  slug: cyble-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 50.6
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyble/refs/heads/main/screenshots/cyble-2026-08-17T080843.png
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
website: https://cyble.com/
---
