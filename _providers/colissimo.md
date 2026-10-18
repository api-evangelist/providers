---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Colissimo Agentic Access
  operation_count: 12
  slug: colissimo-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 4
apis:
- description: Colissimo's delivery-choice / pickup point web service (SOAP) - find pickup and drop-off points by address, coordinates, identifier or token for display in a checkout.
  name: Colissimo Point Retrait API
  slug: colissimo-point-retrait-api
- baseURL: https://ws.colissimo.fr/sls-ws/SlsServiceWSRest/2.0
  baseurl_source: declared
  description: The Description et exemples des méthodes du WS SLS API from Colissimo — 9 operation(s) for description et exemples des méthodes du ws sls.
  name: Colissimo Description et exemples des méthodes du WS SLS API
  slug: colissimo-description-et-exemples-des-m-thodes-du-ws-sls-api
- baseURL: https://ws.colissimo.fr/sls-ws/SlsServiceWSRest/2.0
  baseurl_source: declared
  description: The Génération de bordereau de dépot API from Colissimo — 3 operation(s) for génération de bordereau de dépot.
  name: Colissimo Génération de bordereau de dépot API
  slug: colissimo-g-n-ration-de-bordereau-de-d-pot-api
- baseURL: https://ws.colissimo.fr/sls-ws/SlsServiceWSRest/2.0
  baseurl_source: declared
  description: 'The SlsInternalService : Services destinés aux applications internes API from Colissimo — 3 operation(s) for slsinternalservice : services destinés aux applications internes.'
  name: 'Colissimo SlsInternalService : Services destinés aux applications internes API'
  slug: colissimo-slsinternalservice-services-destin-s-aux-applications-internes-api
- baseURL: https://ws.colissimo.fr/sls-ws/SlsServiceWSRest/2.0
  baseurl_source: declared
  description: 'The SlsServiceWS : documentation API from Colissimo — 9 operation(s) for slsservicews : documentation.'
  name: 'Colissimo SlsServiceWS : documentation API'
  slug: colissimo-slsservicews-documentation-api
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/agentic-access/colissimo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/colissimo-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/rules/colissimo-rules.yml
  title: ''
  type: Spectral
  url: rules/colissimo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/json-ld/colissimo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/colissimo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/vocabulary/colissimo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/colissimo-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/data-model/colissimo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/colissimo-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.laposte.fr/p/Security-Information
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/errors/colissimo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/colissimo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/conformance/colissimo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/colissimo-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/hosts/colissimo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colissimo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/vendors/colissimo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colissimo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/packages/colissimo-packages.yml
  title: ''
  type: SDKs
  url: packages/colissimo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/packages/colissimo-packages.yml
  title: ''
  type: Packages
  url: packages/colissimo-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.colissimo.fr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/security/colissimo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/colissimo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/colissimo/refs/heads/main/security/colissimo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colissimo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.colissimo.fr
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.colissimo.entreprise.laposte.fr/outils-et-solutions
- group: docs
  title: ''
  type: Documentation
  url: https://www.applications.colissimo.entreprise.laposte.fr/doc-colissimo/redoc-sls/fr
- group: operate
  title: ''
  type: Support
  url: https://www.colissimo.entreprise.laposte.fr/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.colissimo.entreprise.laposte.fr/mentions-legales
created: '2026-10-13'
description: Colissimo is La Poste's parcel delivery brand for France and international shipping. For business shippers it publishes developer web services on ws.colissimo.fr - the Shipping Label Service (SLS, web service d'affranchissement) for labels, CN23 customs forms, bordereaux and pickup planning, available as SOAP (WSDL) and REST (OpenAPI), and the Point Retrait web service (SOAP) for finding pickup and drop-off points - documented in Redoc on the Colissimo Entreprise site.
image: https://www.laposte.fr/ecom/_nuxt/logo-part-vertical.BAUyeuwa.svg
json_schemas:
- name: CheckGenerateLabelRequest
  property_count: 6
  slug: colissimo-check-generate-label-request
- name: GenerateLabelRequest
  property_count: 6
  slug: colissimo-generate-label-request
- name: GenerateLabelRequestV31
  property_count: 6
  slug: colissimo-generate-label-request-v31
- name: GetProductInterRequest
  property_count: 9
  slug: colissimo-get-product-inter-request
- name: PlanPickupRequest
  property_count: 5
  slug: colissimo-plan-pickup-request
- name: Response
  property_count: 17
  slug: colissimo-response
jsonld:
- class_count: 71
  name: Colissimo Context
  property_count: 267
  slug: colissimo-context
layout: provider
modified: '2026-10-13'
name: Colissimo
nav: Providers
network: true
overview: 'Colissimo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Description et exemples des méthodes du WS SLS API, Génération de bordereau de dépot API, SlsInternalService : Services destinés aux applications internes API, and 2 more. Tagged areas include Company, Shipping, Logistics, Parcel, and Labels.


  The Colissimo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Colissimo''s developer surface includes documentation, support, and 19 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Colissimo API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: colissimo-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 71.4
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Colissimo Domain Security
  slug: colissimo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Colissimo Vulnerability Disclosure
  slug: colissimo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: colissimo
tags:
- Company
- Shipping
- Logistics
- Parcel
- Labels
- Pickup Points
- France
website: https://www.colissimo.fr
---
