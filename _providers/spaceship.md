---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Spaceship Agentic Access
  operation_count: 40
  slug: spaceship-agentic-access
  summary_line: 40 operations · 23 acting
api_count: 1
apis:
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Async Operations API from Spaceship — 1 operation(s) for async operations.
  name: Spaceship Async Operations API
  slug: spaceship-async-operations-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Contacts API from Spaceship — 2 operation(s) for contacts.
  name: Spaceship Contacts API
  slug: spaceship-contacts-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Contacts attributes API from Spaceship — 2 operation(s) for contacts attributes.
  name: Spaceship Contacts attributes API
  slug: spaceship-contacts-attributes-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The DNS records API from Spaceship — 1 operation(s) for dns records.
  name: Spaceship DNS records API
  slug: spaceship-dns-records-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Domain Availability API from Spaceship — 2 operation(s) for domain availability.
  name: Spaceship Domain Availability API
  slug: spaceship-domain-availability-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Domain Management API from Spaceship — 4 operation(s) for domain management.
  name: Spaceship Domain Management API
  slug: spaceship-domain-management-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Domain Settings API from Spaceship — 5 operation(s) for domain settings.
  name: Spaceship Domain Settings API
  slug: spaceship-domain-settings-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Domain Transfer API from Spaceship — 3 operation(s) for domain transfer.
  name: Spaceship Domain Transfer API
  slug: spaceship-domain-transfer-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The Personal Nameservers API from Spaceship — 2 operation(s) for personal nameservers.
  name: Spaceship Personal Nameservers API
  slug: spaceship-personal-nameservers-api
- baseURL: https://spaceship.dev/api
  baseurl_source: declared
  description: The SellerHub API from Spaceship — 7 operation(s) for sellerhub.
  name: Spaceship SellerHub API
  slug: spaceship-sellerhub-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spaceship.com Async Operations API
  slug: open-spaceship-async-operations-api
- collection_type: open
  name: Spaceship.com Async Operations Contacts API
  slug: open-spaceship-contacts-api
- collection_type: open
  name: Spaceship.com Async Operations Contacts attributes API
  slug: open-spaceship-contacts-attributes-api
- collection_type: open
  name: Spaceship.com Async Operations DNS records API
  slug: open-spaceship-dns-records-api
- collection_type: open
  name: Spaceship.com Async Operations Domain Availability API
  slug: open-spaceship-domain-availability-api
- collection_type: open
  name: Spaceship.com Async Operations Domain Management API
  slug: open-spaceship-domain-management-api
- collection_type: open
  name: Spaceship.com Async Operations Domain Settings API
  slug: open-spaceship-domain-settings-api
- collection_type: open
  name: Spaceship.com Async Operations Domain Transfer API
  slug: open-spaceship-domain-transfer-api
- collection_type: open
  name: Spaceship.com Async Operations Personal Nameservers API
  slug: open-spaceship-personal-nameservers-api
- collection_type: open
  name: Spaceship.com Async Operations SellerHub API
  slug: open-spaceship-sellerhub-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.spaceship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spaceship.com/application/api-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spaceship.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spaceship.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spaceship.dev/
- group: operate
  title: ''
  type: Support
  url: https://www.spaceship.com/about/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spaceshipapp
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaceship-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spaceship-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaceship-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaceship-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaceship-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaceship-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaceship-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spaceship-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaceship-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/spaceship-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaceship-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/spaceship-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceship-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaceship-agentic-access.yml
created: '2026-07-17'
description: Spaceship is a domain registrar and domain marketplace offering domain registration, DNS management, WHOIS privacy protection, and a SellerHub resale marketplace with SafePay escrow. Its public REST API (https://spaceship.dev/api, v1) exposes 40 operations across domain management, availability, settings, transfers, personal nameservers, contacts, DNS records, SellerHub, and asynchronous operations. Authentication uses a paired API key and secret (X-API-Key / X-API-Secret) with per-key scopes; long-running actions use an async-operation polling model (202 + a spaceship-async-operationid header polled at /v1/async-operations/{operationId}).
image: https://spaceship-cdn.com/spaceship-api-doc-assets/logo.svg
layout: provider
modified: '2026-07-21'
name: Spaceship
nav: Providers
network: true
overview: 'Spaceship publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Async Operations API, Contacts API, Contacts attributes API, and 7 more. Tagged areas include Company, Domains, Domain Registrar, DNS, and Domain Marketplace.


  Spaceship''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 15
scopes:
- name: Spaceship Scopes
  scope_count: 11
  slug: spaceship-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.8
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spaceship/refs/heads/main/screenshots/spaceship-2026-09-02T160322.png
security:
- kind: authentication
  name: Spaceship Authentication
  slug: spaceship-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spaceship Domain Security
  slug: spaceship-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: spaceship
tags:
- Company
- Domains
- Domain Registrar
- DNS
- Domain Marketplace
- Nameservers
- WHOIS
- Developer Tools
website: https://www.spaceship.com/
---
