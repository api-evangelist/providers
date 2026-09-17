---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-09-16'
api_count: 4
apis:
- description: Address validation and normalisation against the French Service National de l'Adresse reference base. Autocompletes and corrects addresses as they are typed in signup forms, checkout flows and CRM rec
  name: La Poste ControlAdresse v2
  slug: la-poste-controladresse-v2
- description: Forward geocoding over the La Poste address base - resolve a known postal address to the GPS coordinates La Poste holds for it, for mapping, routing and territory analysis.
  name: La Poste Geolocalisation v1
  slug: la-poste-geolocalisation-v1
- description: Reverse geocoding - given a latitude/longitude pair, returns between one and five nearby French postal addresses within a predefined radius.
  name: La Poste Geolocalisation inversee v1
  slug: la-poste-geolocalisation-inversee-v1
- description: 'Booking API for "Passer mon code avec La Poste" - the official La Poste driving-theory examination service. Covers session lookup, candidate validation, pre-reservations and reservations for both the '
  name: Code de la route v2
  slug: code-de-la-route-v2
- description: Colissimo's SOAP web services for e-commerce shipping - shipping-label and return-label generation, pickup planning, deposit-slip (bordereau) generation, international product lookup, and pickup-point
  name: Colissimo Web Services
  slug: colissimo-web-services
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Administration API from La Poste Groupe — 3 operation(s) for administration.
  name: La Poste Groupe Administration API
  slug: la-poste-groupe-administration-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Applications API from La Poste Groupe — 2 operation(s) for applications.
  name: La Poste Groupe Applications API
  slug: la-poste-groupe-applications-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Digiposte API from La Poste Groupe — 5 operation(s) for digiposte.
  name: La Poste Groupe Digiposte API
  slug: la-poste-groupe-digiposte-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The JDD / Éditable API from La Poste Groupe — 10 operation(s) for jdd / éditable.
  name: La Poste Groupe JDD / Éditable API
  slug: la-poste-groupe-jdd-ditable-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The JDD / Données API from La Poste Groupe — 18 operation(s) for jdd / données.
  name: La Poste Groupe JDD / Données API
  slug: la-poste-groupe-jdd-donn-es-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The JDD / Métadonnées API from La Poste Groupe — 12 operation(s) for jdd / métadonnées.
  name: La Poste Groupe JDD / Métadonnées API
  slug: la-poste-groupe-jdd-m-tadonn-es-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Jeux de données (JDD) API from La Poste Groupe — 1 operation(s) for jeux de données (jdd).
  name: La Poste Groupe Jeux de données (JDD) API
  slug: la-poste-groupe-jeux-de-donn-es-jdd-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The LH PRO resources API from La Poste Groupe — 2 operation(s) for lh pro resources.
  name: La Poste Groupe LH PRO resources API
  slug: la-poste-groupe-lh-pro-resources-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Partner API from La Poste Groupe — 4 operation(s) for partner.
  name: La Poste Groupe Partner API
  slug: la-poste-groupe-partner-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The Resend Purl API from La Poste Groupe — 1 operation(s) for resend purl.
  name: La Poste Groupe Resend Purl API
  slug: la-poste-groupe-resend-purl-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: Everything about one to 10 trackings with or without account's link
  name: La Poste Groupe Suivi API
  slug: la-poste-groupe-suivi-api
- baseURL: https://api.laposte.fr/suivi/v2
  baseurl_source: declared
  description: The User API from La Poste Groupe — 2 operation(s) for user.
  name: La Poste Groupe User API
  slug: la-poste-groupe-user-api
artifact_total: 23
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/overlays/la-poste-groupe-suivi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/la-poste-groupe-suivi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/overlays/la-poste-groupe-digiposte-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/la-poste-groupe-digiposte-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/overlays/la-poste-groupe-lettre-recommandee-en-ligne-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/la-poste-groupe-lettre-recommandee-en-ligne-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/overlays/la-poste-groupe-open-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/la-poste-groupe-open-data-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/security/la-poste-groupe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/la-poste-groupe-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/security/la-poste-groupe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/la-poste-groupe-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/scopes/la-poste-groupe-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/la-poste-groupe-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/authentication/la-poste-groupe-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/packages/la-poste-groupe-packages.yml
  title: ''
  type: Packages
  url: packages/la-poste-groupe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/packages/la-poste-groupe-packages.yml
  title: ''
  type: SDKs
  url: packages/la-poste-groupe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/cli/la-poste-groupe-cli.yml
  title: ''
  type: CLI
  url: cli/la-poste-groupe-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/well-known/la-poste-groupe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/la-poste-groupe-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/well-known/la-poste-groupe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/la-poste-groupe-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/security/la-poste-groupe-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/la-poste-groupe-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/conventions/la-poste-groupe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/la-poste-groupe-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/errors/la-poste-groupe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/la-poste-groupe-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/lifecycle/la-poste-groupe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/la-poste-groupe-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.laposte.fr/status/api
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/conformance/la-poste-groupe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/la-poste-groupe-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/sandbox/la-poste-groupe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/la-poste-groupe-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/data-model/la-poste-groupe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/la-poste-groupe-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/plans/la-poste-groupe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/la-poste-groupe-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/plans/la-poste-groupe-plans-pricing.yml
  title: ''
  type: Pricing
  url: plans/la-poste-groupe-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/rate-limits/la-poste-groupe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/la-poste-groupe-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/la-poste-groupe/refs/heads/main/llms/la-poste-groupe-llms.txt
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
overview: 'La Poste Groupe publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Applications API, Digiposte API, and 9 more. Tagged areas include Company, Logistics, Shipping, Package Tracking, and Postal.


  La Poste Groupe''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, CLI, and 30 more developer resources.'
plans:
- name: La Poste Groupe Plans Pricing
  plan_count: 10
  slug: la-poste-groupe-plans-pricing
random_paper: 12
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
  composite: 66.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 80.4
    discoverability: 81.5
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 64.5
  provenance:
    conformance: derived
    contracts:
      callable: 66.7
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
    score: 75.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Document-Management
- Identity
- Government
- France
website: https://www.lapostegroupe.com/fr
---
