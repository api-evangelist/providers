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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-04'
api_count: 4
apis:
- description: Tenant-scoped REST API for retrieving events, alerts, incidents, audit logs, network and application telemetry, and for managing policies, IoCs, and configuration on the Netskope platform. Authenticat
  name: Netskope REST API v2
  slug: rest-api-v2
- description: SCIM 2.0 provisioning API for users and groups, enabling identity providers and IGA platforms to synchronize directory state into Netskope using a dedicated SCIM token issued from the Security Cloud P
  name: Netskope SCIM API
  slug: scim-api
- baseURL: https://{tenant}.goskope.com/api/v2
  baseurl_source: declared
  description: The Deviceclassification API from Netskope — 1 operation(s) for deviceclassification.
  name: Netskope Deviceclassification API
  slug: netskope-deviceclassification-api
- baseURL: https://{tenant}.goskope.com/api/v2
  baseurl_source: declared
  description: The Scale API from Netskope — 2 operation(s) for scale.
  name: Netskope Scale API
  slug: netskope-scale-api
artifact_total: 8
asyncapis:
- description: ''
  name: Netskope Webhooks
  slug: netskope-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/rules/netskope-rules.yml
  title: ''
  type: Spectral
  url: rules/netskope-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/asyncapi/netskope-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/netskope-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/changelog/netskope-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/netskope-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.netskope.com/vulnerability-disclosure-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/conformance/netskope-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netskope-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/llms/netskope-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netskope-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/well-known/netskope-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netskope-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/well-known/netskope-netskope-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netskope-netskope-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/well-known/netskope-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netskope-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/hosts/netskope-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netskope-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/vendors/netskope-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netskope-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/packages/netskope-packages.yml
  title: ''
  type: SDKs
  url: packages/netskope-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/packages/netskope-packages.yml
  title: ''
  type: Packages
  url: packages/netskope-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.netskope.com/company/newsroom
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netskope.com/en/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/security/netskope-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netskope-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/security/netskope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netskope-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netskopeoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netskope
- group: company
  title: ''
  type: Website
  url: https://www.netskope.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netskope.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.netskope.com/
- group: company
  title: ''
  type: Blog
  url: https://www.netskope.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netskope.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netskope.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.netskope.com/s/
- group: start
  title: ''
  type: Signup
  url: https://www.netskope.com/request-demo
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://community.netskope.com/mcp
  - status: 200
    url: https://www.netskope.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: Netskope is a security service edge (SSE) and SASE platform delivering cloud-native Secure Web Gateway, CASB, Zero Trust Network Access, data loss prevention, and threat protection from its NewEdge global network. The Netskope REST API v2 provides tenant-level programmatic access to events, alerts, incidents, policies, IoCs, SCIM provisioning, and configuration so SOC and platform teams can automate SOAR, SIEM, and IGA workflows using service-account bearer tokens in the Netskope-Api-Token header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netskope.png
layout: provider
modified: '2026-05-11'
name: Netskope
nav: Providers
network: true
overview: 'Netskope publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Deviceclassification API, Scale API, and 2 more. Tagged areas include Security, SASE, SSE, CASB, and Zero Trust.


  The Netskope catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Netskope''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, signup flow, and 21 more developer resources.'
random_paper: 15
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Netskope API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: netskope-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.9
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 17.3
    developer_ergonomics: 45.2
    discoverability: 80.4
    operational_transparency: 36.8
  previous_composite: 12.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/screenshots/netskope-2026-06-20T190208.png
security:
- kind: domain-security
  name: Netskope Domain Security
  slug: netskope-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Netskope Vulnerability Disclosure
  slug: netskope-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: netskope
tags:
- Security
- SASE
- SSE
- CASB
- Zero Trust
- SWG
- DLP
- Cloud Security
website: https://www.netskope.com/
---
