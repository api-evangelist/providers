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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Santevet Agentic Access
  operation_count: 64
  slug: santevet-agentic-access
  summary_line: 64 operations · 9 acting
api_count: 4
apis:
- description: SantéVet's partner quote-to-subscribe funnel and rating engine. Creates and updates prospects (with a dedicated GDPR anonymisation operation), creates, searches, validates and subscribes quotations, a
  name: SantéVet Acquisition API
  slug: santevet-acquisition
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Appareil API from SantéVet — 2 operation(s) for appareil.
  name: SantéVet Appareil API
  slug: santevet-appareil-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Civilite API from SantéVet — 2 operation(s) for civilite.
  name: SantéVet Civilite API
  slug: santevet-civilite-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The ContratRaisonAnnulation API from SantéVet — 2 operation(s) for contratraisonannulation.
  name: SantéVet Contrat Raison Annulation API
  slug: santevet-contratraisonannulation-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Espece API from SantéVet — 2 operation(s) for espece.
  name: SantéVet Espece API
  slug: santevet-espece-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Fractionnement API from SantéVet — 2 operation(s) for fractionnement.
  name: SantéVet Fractionnement API
  slug: santevet-fractionnement-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Langue API from SantéVet — 2 operation(s) for langue.
  name: SantéVet Langue API
  slug: santevet-langue-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The MotifNonRemboursement API from SantéVet — 2 operation(s) for motifnonremboursement.
  name: SantéVet Motif Non Remboursement API
  slug: santevet-motifnonremboursement-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The MotifPeriode API from SantéVet — 2 operation(s) for motifperiode.
  name: SantéVet Motif Periode API
  slug: santevet-motifperiode-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The OrigineCommerciale API from SantéVet — 2 operation(s) for originecommerciale.
  name: SantéVet Origine Commerciale API
  slug: santevet-originecommerciale-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The OrigineConnaissance API from SantéVet — 2 operation(s) for origineconnaissance.
  name: SantéVet Origine Connaissance API
  slug: santevet-origineconnaissance-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Pays API from SantéVet — 2 operation(s) for pays.
  name: SantéVet Pays API
  slug: santevet-pays-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The Race API from SantéVet — 3 operation(s) for race.
  name: SantéVet Race API
  slug: santevet-race-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: Reimbursement
  name: SantéVet Reimbursement API
  slug: santevet-reimbursement-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SinistreMotifRetour API from SantéVet — 2 operation(s) for sinistremotifretour.
  name: SantéVet Sinistre Motif Retour API
  slug: santevet-sinistremotifretour-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The StatutSocialPartenaire API from SantéVet — 2 operation(s) for statutsocialpartenaire.
  name: SantéVet Statut Social Partenaire API
  slug: santevet-statutsocialpartenaire-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvDefContratAssurance API from SantéVet — 3 operation(s) for svdefcontratassurance.
  name: SantéVet Sv Def Contrat Assurance API
  slug: santevet-svdefcontratassurance-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvDefOptionAppliqueeAuDefContrat API from SantéVet — 3 operation(s) for svdefoptionappliqueeaudefcontrat.
  name: SantéVet Sv Def Option Appliquee Au Def Contrat API
  slug: santevet-svdefoptionappliqueeaudefcontrat-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvGroupeRace API from SantéVet — 2 operation(s) for svgrouperace.
  name: SantéVet Sv Groupe Race API
  slug: santevet-svgrouperace-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvMarqueTel API from SantéVet — 3 operation(s) for svmarquetel.
  name: SantéVet Sv Marque Tel API
  slug: santevet-svmarquetel-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvPromo API from SantéVet — 2 operation(s) for svpromo.
  name: SantéVet Sv Promo API
  slug: santevet-svpromo-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The SvTarifsContrat API from SantéVet — 2 operation(s) for svtarifscontrat.
  name: SantéVet Sv Tarifs Contrat API
  slug: santevet-svtarifscontrat-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The TypeIdentifiantOfficielPartenaire API from SantéVet — 2 operation(s) for typeidentifiantofficielpartenaire.
  name: SantéVet Type Identifiant Officiel Partenaire API
  slug: santevet-typeidentifiantofficielpartenaire-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The TypeOption API from SantéVet — 2 operation(s) for typeoption.
  name: SantéVet Type Option API
  slug: santevet-typeoption-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The TypePartenaire API from SantéVet — 2 operation(s) for typepartenaire.
  name: SantéVet Type Partenaire API
  slug: santevet-typepartenaire-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The TypeReglement API from SantéVet — 2 operation(s) for typereglement.
  name: SantéVet Type Reglement API
  slug: santevet-typereglement-api
- baseURL: https://toolkit.api.santevet.com
  baseurl_source: declared
  description: The TypeSinistre API from SantéVet — 2 operation(s) for typesinistre.
  name: SantéVet Type Sinistre API
  slug: santevet-typesinistre-api
artifact_total: 33
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/santevet-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/santevet-toolkit-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/santevet-reimbursement-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.santevet.com/
- group: start
  title: ''
  type: Login
  url: https://espaceclient.santevet.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.santevet.com/partenaire-btob
- group: operate
  title: ''
  type: Support
  url: https://www.santevet.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.santevet.com/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santevet.com/mes-donnees-personnelles
- group: auth
  title: ''
  type: Authentication
  url: authentication/santevet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/santevet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/santevet-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/santevet-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/santevet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/santevet-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santevet-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/santevet-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/santevet-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/santevet-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/santevet-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/santevet-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/santevet-agentic-access.yml
created: '2026-08-17'
description: 'SantéVet is a French pet-insurance company, founded in 2003 and headquartered in Lyon, that insures dogs, cats and small pets (NAC) across five European markets — France, Belgium, Spain, Italy and Germany. Alongside its direct-to-consumer business it runs a B2B distribution network: brokers, retailers, affinity partners and veterinary practices embed SantéVet quoting, subscription and claims into their own channels over HTTP APIs. Three of those partner APIs serve documentation anonymously — a reference-data Toolkit API (58 operations, API Platform, Hydra/JSON-LD), a Reimbursement API behind the PayVet third-party-payment product (6 operations, OpenAPI 3.0.3), and an Acquisition API carrying the quote-to-subscribe funnel and the rating engine (14 operations, HTML reference only). SantéVet publishes no developer portal, no SDK, no pricing and no self-serve signup; credentials are issued through a sales process.'
jsonld:
- class_count: 0
  name: Santevet Toolkit Hydra Docs Context
  property_count: 5
  slug: santevet-toolkit-hydra-docs
layout: provider
modified: '2026-08-17'
name: SantéVet
nav: Providers
network: true
overview: 'SantéVet publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Appareil API, Civilite API, Contrat Raison Annulation API, and 23 more. Tagged areas include Insurance, Insurtech, Pet Insurance, Veterinary, and Consumer.


  The SantéVet catalog on APIs.io includes 1 JSON-LD context.


  SantéVet''s developer surface includes signup flow, support, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Santevet Plans Pricing
  plan_count: 0
  slug: santevet-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Santevet Rate Limits
  slug: santevet-rate-limits
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 32.7
    discoverability: 77.8
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 3.8
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/santevet/refs/heads/main/screenshots/santevet-2026-09-02T154405.png
security:
- kind: authentication
  name: Santevet Authentication
  slug: santevet-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Santevet Domain Security
  slug: santevet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santevet
tags:
- Insurance
- Insurtech
- Pet Insurance
- Veterinary
- Consumer
- Embedded Insurance
- Claims
- Payments
- France
- Europe
- Company
website: https://www.santevet.com/
---
