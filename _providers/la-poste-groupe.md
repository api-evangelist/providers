---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-04'
api_count: 9
apis:
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: Real-time tracking for La Poste shipments. Suivi v2 harmonises the delivery status of tracked mail (courrier suivi), Colissimo parcels and Chronopost express into one simplified status plus the full r
  name: La Poste Suivi v2
  slug: la-poste-suivi-v2
- description: Address validation and normalisation against the French Service National de l'Adresse reference base. Autocompletes and corrects addresses as they are typed in signup forms, checkout flows and CRM rec
  name: La Poste ControlAdresse v2
  slug: la-poste-controladresse-v2
- description: Forward geocoding over the La Poste address base - resolve a known postal address to the GPS coordinates La Poste holds for it, for mapping, routing and territory analysis.
  name: La Poste Geolocalisation v1
  slug: la-poste-geolocalisation-v1
- description: Reverse geocoding - given a latitude/longitude pair, returns between one and five nearby French postal addresses within a predefined radius.
  name: La Poste Geolocalisation inversee v1
  slug: la-poste-geolocalisation-inversee-v1
- baseURL: https://api.laposte.fr/digiposte/v3
  baseurl_source: declared
  description: 'Partner API for Digiposte+, La Poste''s certified digital safe (coffre-fort numerique a valeur probante). Lets an issuer create and manage memberships, deposit certified documents into a user''s vault, '
  name: Digiposte v3
  slug: digiposte-v3
- baseURL: https://api-order-lh-pro-ct-sacc.paas-01.build.net.intra.laposte.fr
  baseurl_source: spec
  description: 'Online registered-mail ordering. Businesses submit a registered letter through the API and La Poste prints it, folds and inserts it, franks it and delivers it, then returns a proof of deposit (preuve '
  name: Lettre recommandee en ligne v1
  slug: lettre-recommandee-en-ligne-v1
- description: 'Booking API for "Passer mon code avec La Poste" - the official La Poste driving-theory examination service. Covers session lookup, candidate validation, pre-reservations and reservations for both the '
  name: Code de la route v2
  slug: code-de-la-route-v2
- baseURL: https://api.laposte.fr/opendata/v1
  baseurl_source: declared
  description: Gateway over La Poste's open datasets - postal codes (hexasmal), contact points, post-office opening hours, services and accessibility, street letterboxes, self-service machines and new communes. Fron
  name: La Poste Open Data v1
  slug: la-poste-open-data-v1
- description: Colissimo's SOAP web services for e-commerce shipping - shipping-label and return-label generation, pickup planning, deposit-slip (bordereau) generation, international product lookup, and pickup-point
  name: Colissimo Web Services
  slug: colissimo-web-services
artifact_total: 15
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/la-poste-groupe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-poste-groupe-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/la-poste-groupe-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/la-poste-groupe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lapostegroupe.com/fr
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.laposte.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation-okapi.laposte.fr/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.laposte.fr/catalog-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.laposte.fr/getting-started
- group: operate
  title: ''
  type: Support
  url: https://faq.developer.laposte.fr
- group: company
  title: ''
  type: Blog
  url: https://www.lapostegroupe.com/fr/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeveloperLaPoste
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.laposte.fr/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.laposte.fr/data-privacy
- group: build
  title: ''
  type: Postman
  url: https://github.com/DeveloperLaPoste/okapi-postman
- group: build
  title: ''
  type: Packages
  url: packages/la-poste-groupe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/la-poste-groupe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/la-poste-groupe-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/la-poste-groupe-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/la-poste-groupe-security.txt
- group: auth
  title: ''
  type: Security
  url: security/la-poste-groupe-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/la-poste-groupe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/la-poste-groupe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/la-poste-groupe-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.laposte.fr/status/api
- group: design
  title: ''
  type: Conformance
  url: conformance/la-poste-groupe-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/la-poste-groupe-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/la-poste-groupe-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/la-poste-groupe-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: plans/la-poste-groupe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/la-poste-groupe-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/la-poste-groupe-llms.txt
created: '2026-09-02'
description: 'La Poste Groupe is the French state-owned postal, parcel, banking and digital services group. Its public API programme runs on Okapi, the group''s own API management platform, published at developer.laposte.fr: nine APIs covering shipment tracking across mail, Colissimo and Chronopost (Suivi v2), address validation and normalisation (ControlAdresse v2), forward and reverse geocoding, the Digiposte certified digital-safe partner API, online registered mail (Lettre recommandee en ligne), driving-licence exam booking (Code de la route) and an Open Data gateway over data.laposte.fr. Colissimo, the group''s parcel arm, additionally publishes SOAP contracts for label generation and pickup-point lookup at ws.colissimo.fr, and GeoPost/DPDgroup sits inside the same group. Access is metered by subscription plans with published quotas and prices, and calls are authenticated with an X-Okapi-Key header against the api.laposte.fr gateway.'
image: https://developer.laposte.fr/apple-touch-icon.png
layout: provider
modified: '2026-09-02'
name: La Poste Groupe
nav: Providers
network: true
overview: 'La Poste Groupe publishes 4 APIs on the [APIs.io](https://apis.io/) network, including La Poste Suivi v2, Digiposte v3, Lettre recommandee en ligne v1, and 1 more. Tagged areas include Company, Logistics, Shipping, Package Tracking, and Postal.


  La Poste Groupe''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, CLI, and 26 more developer resources.'
plans:
- name: La Poste Groupe Plans Pricing
  plan_count: 10
  slug: la-poste-groupe-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: La Poste Groupe Rate Limits
  slug: la-poste-groupe-rate-limits
scopes:
- name: La Poste Groupe Scopes
  scope_count: 0
  slug: la-poste-groupe-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 85.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 65.8
  provenance:
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: La Poste Groupe Authentication
  slug: la-poste-groupe-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: La Poste Groupe Domain Security
  slug: la-poste-groupe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: La Poste Groupe Vulnerability Disclosure
  slug: la-poste-groupe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: la-poste-groupe
tags:
- Company
- Logistics
- Shipping
- Package Tracking
- Postal
- Addresses
- Geocoding
- Open Data
- Document Management
- Identity
- Government
- France
website: https://www.lapostegroupe.com/fr
---
