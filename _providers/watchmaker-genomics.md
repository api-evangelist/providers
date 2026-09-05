---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The Adobe Commerce (Magento 2) storefront GraphQL API instantiated on Watchmaker Genomics' own host. Fully introspectable without credentials — 636 types, 54 root query fields and 99 mutations coverin
  name: Watchmaker Genomics Storefront GraphQL API
  slug: watchmaker-genomics-storefront-graphql-api
- baseURL: https://www.watchmakergenomics.com/rest/all
  baseurl_source: declared
  description: The Adobe Commerce REST API on Watchmaker Genomics' own host, self-describing at /rest/all/schema?services=all as a Swagger 2.0 document with 61 paths and 70 operations. The anonymous slice — director
  name: Watchmaker Genomics Storefront REST API
  slug: watchmaker-genomics-storefront-rest-api
- description: The Adobe Commerce SOAP surface on Watchmaker Genomics' own host. /soap/all?wsdl_list=1 enumerates 200 services and each returns a WSDL 1.1 contract whose target namespace is https://www.watchmakergen
  name: Watchmaker Genomics Storefront SOAP API
  slug: watchmaker-genomics-storefront-soap-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.watchmakergenomics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.watchmakergenomics.com/find-a-resource-or-tool
- group: operate
  title: ''
  type: Support
  url: https://www.watchmakergenomics.com/technical-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.watchmakergenomics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.watchmakergenomics.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.watchmakergenomics.com/request-quote
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/watchmaker-genomics
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/watchmaker-genomics-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/watchmaker-genomics-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/watchmaker-genomics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/watchmaker-genomics-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/watchmaker-genomics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/watchmaker-genomics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/watchmaker-genomics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/watchmaker-genomics-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/watchmaker-genomics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/watchmaker-genomics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/watchmaker-genomics-domain-security.yml
created: '2026-09-04'
description: 'Watchmaker Genomics is a Boulder, Colorado life-science company that engineers and manufactures high-performance enzymes and next-generation-sequencing library preparation kits for clinical, translational and molecular-diagnostics workflows — DNA and RNA library prep, TAPS+ methylation sequencing, EquiPlex normalization, Equinox Prime amplification, high-fidelity polymerases, reverse transcriptases and MDx reagents. It is a reagents manufacturer rather than an API company: it runs no developer program and publishes no API documentation, but its Adobe Commerce (Magento 2) storefront at www.watchmakergenomics.com serves a live, publicly introspectable GraphQL endpoint, a Swagger 2.0 REST schema and 200 SOAP WSDL services over its own product catalog, and its GitHub organization publishes first-party bioinformatics tools including the TAPS+ Variant Caller (TVC).'
image: https://www.watchmakergenomics.com/media/codazon/logo/22/default/Watchmaker_Logo_RGB_Wtext_500px.png
layout: provider
modified: '2026-09-04'
name: Watchmaker Genomics
nav: Providers
network: true
overview: 'Watchmaker Genomics publishes 1 API on the [APIs.io](https://apis.io/) network: Storefront REST API. Tagged areas include Genomics, Life Sciences, Next-Generation Sequencing, Molecular Diagnostics, and Biotechnology.


  Watchmaker Genomics'' developer surface includes documentation, support, pricing, CLI, and 15 more developer resources.'
plans:
- name: Watchmaker Genomics Plans Pricing
  plan_count: 0
  slug: watchmaker-genomics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Watchmaker Genomics Rate Limits
  slug: watchmaker-genomics-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 41.5
    developer_ergonomics: 35.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Watchmaker Genomics Authentication
  slug: watchmaker-genomics-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Watchmaker Genomics Domain Security
  slug: watchmaker-genomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: watchmaker-genomics
tags:
- Genomics
- Life Sciences
- Next-Generation Sequencing
- Molecular Diagnostics
- Biotechnology
- Reagents
- Bioinformatics
- E-Commerce
- GraphQL
- Adobe Commerce
website: https://www.watchmakergenomics.com/
---
