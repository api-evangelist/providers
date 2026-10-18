---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Logius Agentic Access
  operation_count: 24
  slug: logius-agentic-access
  summary_line: 24 operations · 13 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Digipoort is the Logius electronic post office for exchanging messages between businesses and Dutch government bodies (e.g. Belastingdienst, SBR filings). Its WUS 2.0 SOAP interface for businesses off
  name: Digipoort WUS 2.0 voor bedrijven
  slug: digipoort-wus-2-0-bedrijven
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Announce API from Logius — 1 operation(s) for announce.
  name: Logius Announce API
  slug: logius-announce-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Contracts API from Logius — 2 operation(s) for contracts.
  name: Logius Contracts API
  slug: logius-contracts-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The domains API from Logius — 2 operation(s) for domains.
  name: Logius Domains API
  slug: logius-domains-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The events API from Logius — 1 operation(s) for events.
  name: Logius Events API
  slug: logius-events-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The manager API from Logius — 3 operation(s) for manager.
  name: Logius Manager API
  slug: logius-manager-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Peers API from Logius — 1 operation(s) for peers.
  name: Logius Peers API
  slug: logius-peers-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Services API from Logius — 1 operation(s) for services.
  name: Logius Services API
  slug: logius-services-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The subscriptions API from Logius — 2 operation(s) for subscriptions.
  name: Logius Subscriptions API
  slug: logius-subscriptions-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Terugmelding API from Logius — 1 operation(s) for terugmelding.
  name: Logius Terugmelding API
  slug: logius-terugmelding-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The TerugmeldingStatus API from Logius — 1 operation(s) for terugmeldingstatus.
  name: Logius Terugmelding Status API
  slug: logius-terugmeldingstatus-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The Token API from Logius — 1 operation(s) for token.
  name: Logius Token API
  slug: logius-token-api
- baseURL: https://dgp.procesinfrastructuur.nl/wus/2.0
  baseurl_source: declared
  description: The .well Known API from Logius — 1 operation(s) for .well known.
  name: Logius .well Known API
  slug: logius-well-known-api
artifact_total: 34
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/well-known/logius-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/logius-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/agentic-access/logius-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logius-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/plans/logius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logius-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/rules/logius-rules.yml
  title: ''
  type: Spectral
  url: rules/logius-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/rules/logius-publicatie-preview-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/logius-publicatie-preview-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/rules/logius-publicatie-preview-api-design-rules-release-2-2-media-linte-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/logius-publicatie-preview-api-design-rules-release-2-2-media-linte-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/rules/logius-api-design-rules-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/logius-api-design-rules-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/json-ld/logius-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/logius-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/vocabulary/logius-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/logius-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/data-model/logius-data-model.yml
  title: ''
  type: DataModel
  url: data-model/logius-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/components/logius-components.yml
  title: ''
  type: Components
  url: components/logius-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/changelog/logius-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/logius-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/conventions/logius-conventions.yml
  title: ''
  type: Conventions
  url: conventions/logius-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/sandbox/logius-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/logius-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/lifecycle/logius-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/logius-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/lifecycle/logius-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/logius-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/errors/logius-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/logius-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/errors/logius-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/logius-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/conformance/logius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logius-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/overlays/logius-fsc-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/logius-fsc-manager-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/well-known/logius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/logius-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/well-known/logius-logius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/logius-logius-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/well-known/logius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/logius-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/hosts/logius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logius-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/vendors/logius-vendors.yml
  title: ''
  type: Vendors
  url: vendors/logius-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/packages/logius-packages.yml
  title: ''
  type: SDKs
  url: packages/logius-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/packages/logius-packages.yml
  title: ''
  type: Packages
  url: packages/logius-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/authentication/logius-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logius-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/security/logius-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/logius-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/security/logius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://schema.org/docs/schemas.html
- group: docs
  title: NLgov REST API Design Rules
  type: Documentation
  url: https://logius-standaarden.github.io/API-Design-Rules/
- group: other
  title: ''
  type: APIStandards
  url: https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/api-standaarden
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Logius-standaarden
- group: company
  title: Actueel (news)
  type: Blog
  url: https://www.logius.nl/actueel
- group: operate
  title: ''
  type: Support
  url: https://www.logius.nl/contact
- group: operate
  title: Storingen en onderhoud (outages and maintenance)
  type: StatusPage
  url: https://www.logius.nl/storingen-en-onderhoud
- group: commercial
  title: Tarieven (service fees)
  type: Pricing
  url: https://www.logius.nl/zakendoen-met-logius/tarieven
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logius.nl/privacyverklaring
- group: auth
  title: Kwetsbaarheden of problemen melden (vulnerability reporting)
  type: Security
  url: https://www.logius.nl/kwetsbaarheden-problemen-melden
- group: company
  title: ''
  type: About
  url: https://www.logius.nl/about-logius
- group: company
  title: ''
  type: LinkedIn
  url: https://nl.linkedin.com/company/logius
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Logius_minbzk
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/Logius-standaarden/API-Design-Rules/blob/27297e8e45282aeeddb31c011965b5e377b02d6f/media/linter.yaml
created: '2026-10-09'
description: Logius is the digital government service organisation of the Dutch Ministry of the Interior and Kingdom Relations (Ministerie van Binnenlandse Zaken en Koninkrijksrelaties). It provides the shared ICT infrastructure and standards used by Dutch public service providers, including DigiD, eHerkenning, MijnOverheid, Digipoort, Digikoppeling, PKIoverheid and Standard Business Reporting, and it maintains the NL GOV REST API Design Rules and related API standards (with a Spectral linter ruleset) for the Dutch public sector.
image: https://www.logius.nl/themes/custom/logius/logo.svg
json_schemas:
- name: contractContent
  property_count: 7
  slug: logius-contract-content
- name: contract
  property_count: 2
  slug: logius-contract
- name: Domain
  property_count: 5
  slug: logius-domain
- name: enabledExtensions
  property_count: 2
  slug: logius-enabled-extensions
- name: Event
  property_count: 16
  slug: logius-event
- name: jwks
  property_count: 1
  slug: logius-jwks
- name: Ontvangen
  property_count: 4
  slug: logius-ontvangen
- name: peer
  property_count: 3
  slug: logius-peer
- name: serviceListing
  property_count: 1
  slug: logius-service-listing
- name: SubscriptionRequest
  property_count: 10
  slug: logius-subscription-request
- name: Subscription
  property_count: 0
  slug: logius-subscription
- name: TerugMelding
  property_count: 2
  slug: logius-terug-melding
jsonld:
- class_count: 56
  name: Logius Context
  property_count: 101
  slug: logius-context
layout: provider
modified: '2026-10-09'
name: Logius
nav: Providers
network: true
overview: 'Logius publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Announce API, Contracts API, Domains API, and 10 more. Tagged areas include Company, Government, Netherlands, API Standards, and API Design Rules.


  The Logius catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Logius'' developer surface includes changelog, sandbox, authentication, documentation, engineering blog, support, pricing, and 38 more developer resources.'
plans:
- name: Logius Plans Pricing
  plan_count: 4
  slug: logius-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Logius Rate Limits
  slug: logius-rate-limits
rules:
- authorship: provider
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Logius — api design rules rules
  rule_count: 24
  severity_counts:
    error: 24
    hint: 0
    info: 0
    warn: 0
  slug: logius-api-design-rules-spectral-rules
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Logius API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 2
  slug: logius-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 91.3
    catalog_earned_first_party: 30.0
    catalog_gap: 23.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 52.6
    contract_governance: 76.5
    contract_quality: 57.9
    developer_ergonomics: 44.6
    discoverability: 71.4
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/logius/refs/heads/main/screenshots/logius-2026-10-11T110547.png
security:
- kind: authentication
  name: Logius Authentication
  slug: logius-authentication
  summary_line: http/mutualTLS · 3 schemes
- kind: domain-security
  name: Logius Domain Security
  slug: logius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Logius Vulnerability Disclosure
  slug: logius-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: logius
tags:
- Company
- Government
- Netherlands
- API Standards
- API Design Rules
- Digital Identity
- Data Exchange
- Public Sector
website: https://schema.org/docs/schemas.html
---
