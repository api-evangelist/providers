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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Basile Cc Agentic Access
  operation_count: 16
  slug: basile-cc-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.basile.cc
  baseurl_source: declared
  description: 'E-mail et numéro de n''importe quelle personne, dans Basile ou non, payés sur le solde d''enrichissement : 5 centimes par e-mail trouvé, 50 centimes par numéro trouvé, rien si rien n''est trouvé. En deux'
  name: Basile Enrichissement API
  slug: basile-cc-enrichissement-api
- baseURL: https://api.basile.cc
  baseurl_source: declared
  description: Recherche et export de sociétés (registre + LinkedIn + Google My Business).
  name: Basile Entreprises API
  slug: basile-cc-entreprises-api
- baseURL: https://api.basile.cc
  baseurl_source: declared
  description: Recherche et export de contacts (dirigeants légaux + profils LinkedIn).
  name: Basile Personnes API
  slug: basile-cc-personnes-api
- baseURL: https://api.basile.cc
  baseurl_source: declared
  description: Autocomplétion pour trouver les valeurs valides des filtres.
  name: Basile Suggestions API
  slug: basile-cc-suggestions-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/basile-cc/agentic-access/basile-cc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/basile-cc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/rules/basile-cc-rules.yml
  title: ''
  type: Spectral
  url: rules/basile-cc-rules.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/json-ld/basile-cc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/basile-cc-context.jsonld
- group: design
  href: https://artifacts.apis.io/basile-cc/vocabulary/basile-cc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/basile-cc-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/basile-cc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/data-model/basile-cc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basile-cc-data-model.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/conventions/basile-cc-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/basile-cc-conventions.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/conventions/basile-cc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/basile-cc-conventions.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/errors/basile-cc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/basile-cc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/basile-cc/conformance/basile-cc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basile-cc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basile-cc/llms/basile-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basile-cc-llms.txt
- group: agent
  href: https://artifacts.apis.io/basile-cc/well-known/basile-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basile-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/basile-cc/hosts/basile-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basile-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/basile-cc/vendors/basile-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basile-cc-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.basile.cc/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.basile.cc/
- group: auth
  href: https://artifacts.apis.io/basile-cc/authentication/basile-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/basile-cc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/basile-cc/security/basile-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basile-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.basile.cc/
created: '2026-11-02'
description: Basile is a French B2B data platform offering a database of 27 million companies and 29.2 million contacts. It aggregates legal data, Google Maps, LinkedIn and public sources to generate qualified leads. Users can search, filter and export data with a free trial of 100 contacts.
image: https://www.basile.cc/og-image.png
jsonld:
- class_count: 20
  name: Basile Cc Context
  property_count: 154
  slug: basile-cc-context
layout: provider
modified: '2026-11-02'
name: Basile
nav: Providers
network: true
overview: 'Basile publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enrichissement API, Entreprises API, Personnes API, and 1 more. Tagged areas include Company, B2B, Data, Leads, and French.


  The Basile catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Basile''s developer surface includes engineering blog, API reference, authentication, and 16 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Basile API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 4
  slug: basile-cc-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.4
    developer_ergonomics: 18.5
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Basile Cc Authentication
  slug: basile-cc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Basile Cc Domain Security
  slug: basile-cc-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: basile-cc-enrich
  slug: basile-cc-enrich
slug: basile-cc
tags:
- Company
- B2B
- Data
- Leads
- French
- Software-as-a-Service
website: https://www.basile.cc/
---
