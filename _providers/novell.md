---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST/JSON administration API for a GroupWise system, served by the GroupWise Administration Service that installs alongside the GroupWise agents. Introduced under the "Windermere" codename for GroupWi
  name: GroupWise Administration REST API
  slug: groupwise-administration-rest-api
- description: Server-side SOAP protocol for reading and writing a GroupWise user's mailbox, spoken directly to the GroupWise Post Office Agent over HTTP/HTTPS. 96 documented methods defined in the methods.xsd schem
  name: GroupWise Web Services (SOAP)
  slug: groupwise-web-services-soap
- description: DSML v2 for eDirectory ships a deployable Java web archive (.war) that exposes Novell eDirectory as a SOAP web service using DSML - the OASIS Directory Services Markup Language standard for representi
  name: DSML for eDirectory (SOAP)
  slug: dsml-for-edirectory-soap
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.novell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.novell.com/developer/ndk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.novell.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.novell.com/documentation/developer/groupwise_sdk/
- group: build
  href: https://artifacts.apis.io/novell/packages/novell-packages.yml
  title: ''
  type: Packages
  url: packages/novell-packages.yml
- group: build
  href: https://artifacts.apis.io/novell/packages/novell-packages.yml
  title: ''
  type: SDKs
  url: packages/novell-packages.yml
- group: auth
  href: https://artifacts.apis.io/novell/authentication/novell-authentication.yml
  title: ''
  type: Authentication
  url: authentication/novell-authentication.yml
- group: design
  href: https://artifacts.apis.io/novell/conformance/novell-conformance.yml
  title: ''
  type: Conformance
  url: conformance/novell-conformance.yml
- group: design
  href: https://artifacts.apis.io/novell/conventions/novell-conventions.yml
  title: ''
  type: Conventions
  url: conventions/novell-conventions.yml
- group: design
  href: https://artifacts.apis.io/novell/errors/novell-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/novell-error-codes.yml
- group: design
  href: https://artifacts.apis.io/novell/data-model/novell-data-model.yml
  title: ''
  type: DataModel
  url: data-model/novell-data-model.yml
- group: design
  href: https://artifacts.apis.io/novell/lifecycle/novell-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/novell-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.microfocus.com/lifecycle/
- group: operate
  href: https://artifacts.apis.io/novell/changelog/novell-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/novell-changelog.yml
- group: agent
  href: https://artifacts.apis.io/novell/llms/novell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/novell-llms.txt
- group: commercial
  href: https://artifacts.apis.io/novell/plans/novell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/novell-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/novell/rate-limits/novell-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/novell-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/novell/security/novell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/novell-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/novell/security/novell-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/novell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://support.novell.com/security-alerts/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.novell.com/developer/ndk/groupwise/develop_to_groupwise.html
created: '2026-09-13'
description: 'Novell, Inc. was a Provo, Utah network-software company best known for NetWare, eDirectory, GroupWise and ZENworks. It was acquired by The Attachmate Group in 2011, folded into Micro Focus with the 2014 Attachmate acquisition, and passed to OpenText when OpenText bought Micro Focus in 2023. The Novell corporate brand is retired and novell.com is now an OpenText-operated redirector, but a large part of the Novell developer surface is still served on www.novell.com and is not merely archival: the Novell Developer Kit (NDK) A-Z index, the eDirectory developer kits (which now 301 to microfocus.com), and the GroupWise SDK documentation set published per release right up to GroupWise 25. Two callable API surfaces are documented there - the GroupWise Administration REST API (220 resource paths, 357 operations, served by the customer''s own GroupWise Administration Service on port 9710) and the GroupWise Web Services SOAP protocol against the Post Office Agent (96 documented methods
  on port 7191). Both are customer-hosted, not SaaS: there is no Novell-operated endpoint, no key to obtain and no sign-up. No machine-readable contract is obtainable - a WSDL is referenced by name but shipped only inside SDK archives on hosts that no longer resolve, and the Admin API''s WADL is generated at runtime on the customer''s own server. The documentation outlived the distribution.'
image: https://www.novell.com/favicon.ico
layout: provider
modified: '2026-09-13'
name: Novell
nav: Providers
network: true
overview: 'Novell is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Software, Collaboration, Email, and Directory Services.


  Novell''s developer surface includes documentation, API reference, authentication, changelog, getting-started guide, and 16 more developer resources.'
plans:
- name: Novell Plans Pricing
  plan_count: 0
  slug: novell-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Novell Rate Limits
  slug: novell-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 34.2
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/novell/novell-2026-10-11T111650.png
security:
- kind: authentication
  name: Novell Authentication
  slug: novell-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Novell Domain Security
  slug: novell-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Novell Vulnerability Disclosure
  slug: novell-vulnerability-disclosure
  summary_line: no policy recorded
slug: novell
tags:
- Company
- Enterprise Software
- Collaboration
- Email
- Directory Services
- Identity
- groupware
- LDAP
- SOAP
- Legacy
- Self-Hosted
- Endpoint Management
website: https://www.novell.com/
---
