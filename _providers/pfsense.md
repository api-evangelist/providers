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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pfsense Agentic Access
  operation_count: 12
  slug: pfsense-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 1
apis:
- description: Community-maintained REST and GraphQL API package for pfSense CE and pfSense Plus exposing 200+ endpoints under /api/v2 for firewall, interface, service, user, and system management. Authentication su
  name: pfSense REST API (pfSense-pkg-RESTAPI)
  slug: rest-api-package
- baseURL: https://pfsense.local/api/v2
  baseurl_source: declared
  description: Obtain JWT bearer tokens.
  name: pfSense Authentication API
  slug: pfsense-authentication-api
- baseURL: https://pfsense.local/api/v2
  baseurl_source: declared
  description: Manage firewall aliases.
  name: pfSense Firewall Aliases API
  slug: pfsense-firewall-aliases-api
- baseURL: https://pfsense.local/api/v2
  baseurl_source: declared
  description: Apply pending firewall changes.
  name: pfSense Firewall Apply API
  slug: pfsense-firewall-apply-api
- baseURL: https://pfsense.local/api/v2
  baseurl_source: declared
  description: Manage firewall rules.
  name: pfSense Firewall Rules API
  slug: pfsense-firewall-rules-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI) Authentication API
  slug: open-pfsense-authentication-api
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI) Authentication Firewall Aliases API
  slug: open-pfsense-firewall-aliases-api
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI) Authentication Firewall Apply API
  slug: open-pfsense-firewall-apply-api
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI) Authentication Firewall Rules API
  slug: open-pfsense-firewall-rules-api
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI)
  slug: open-pfsense
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jaredhendrickson13/pfsense-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jaredhendrickson13/pfsense-api/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pfrest/pfSense-pkg-RESTAPI/blob/master/docs/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/jaredhendrickson13/pfsense-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pfsense-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pfsense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pfsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pfsense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pfsense.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netgate.com/pfsense/en/latest/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netgate.com/pfsense-plus-software
- group: other
  title: ''
  type: Download
  url: https://www.pfsense.org/download/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pfsense
- group: other
  title: ''
  type: Vendor
  url: https://www.netgate.com/
- group: company
  title: ''
  type: Blog
  url: https://www.netgate.com/blog/rss.xml
created: '2026-05-11'
description: pfSense is an open-source firewall and router operating system based on FreeBSD, developed and maintained by Netgate, providing stateful firewall, routing, VPN (IPsec, OpenVPN, WireGuard), captive portal, traffic shaping, and IDS/IPS capabilities for home and enterprise networks. It is available as pfSense Community Edition (CE) and pfSense Plus, both managed via a web UI. The unofficial pfSense-pkg-RESTAPI package adds a REST and GraphQL API with 200+ endpoints under /api/v2 for automating firewall management, authenticated via local users, API keys, or JWT.
graphqls:
- description: Community-maintained REST and GraphQL API package for pfSense CE and pfSense Plus exposing 200+ endpoints under /api/v2 for firewall, interface, service, user, and system management. Authentication su
  name: pfSense GraphQL API
  slug: pfsense-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pfsense.png
layout: provider
modified: '2026-05-11'
name: pfSense
nav: Providers
network: true
overview: 'pfSense publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Firewall Aliases API, Firewall Apply API, and 1 more. Tagged areas include Firewall, Network Security, Router, VPN, and Open-Source.


  pfSense''s developer surface includes authentication, documentation, pricing, engineering blog, and 11 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pfsense/refs/heads/main/screenshots/pfsense-2026-06-20T191628.png
security:
- kind: authentication
  name: Pfsense Authentication
  slug: pfsense-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Pfsense Domain Security
  slug: pfsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pfsense Vulnerability Disclosure
  slug: pfsense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pfsense
tags:
- Firewall
- Network Security
- Router
- VPN
- Open-Source
- FreeBSD
- Netgate
website: https://www.pfsense.org/
---
