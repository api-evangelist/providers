---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The publishing half of the standard — the JSON manifest a domain serves at /.well-known/ai-catalog.json declaring who the host is and what agentic resources it offers, each entry typed by media type, '
  name: AI Catalog Manifest
  slug: ai-catalog-manifest
- description: The Agents API from Agentic Resource Discovery (ARD) — 1 operation(s) for agents.
  name: Agentic Resource Discovery (ARD) Agents API
  slug: agentic-resource-discovery-agents-api
- description: The Explore API from Agentic Resource Discovery (ARD) — 1 operation(s) for explore.
  name: Agentic Resource Discovery (ARD) Explore API
  slug: agentic-resource-discovery-explore-api
- description: The Search API from Agentic Resource Discovery (ARD) — 1 operation(s) for search.
  name: Agentic Resource Discovery (ARD) Search API
  slug: agentic-resource-discovery-search-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Agent-Card/ai-catalog/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Agent-Card/ai-catalog/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Agent-Card/ai-catalog/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Agent-Card/ai-catalog/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://agenticresourcediscovery.org
- group: docs
  title: ''
  type: Specification
  url: https://agenticresourcediscovery.org/spec/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ards-project/ard-spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ards-project
- group: commercial
  title: ''
  type: License
  url: https://github.com/ards-project/ard-spec/blob/main/LICENSE
- group: other
  title: ''
  type: Contributing
  url: https://github.com/ards-project/ard-spec#contributing
- group: other
  title: ''
  type: Participants
  url: https://agenticresourcediscovery.org/contributors/
- group: other
  title: ''
  type: Governance
  url: governance/agentic-resource-discovery-governance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentic-resource-discovery-conformance.yml
- group: other
  title: ''
  type: TestSuite
  url: https://github.com/ards-project/ard-spec/tree/main/conformance
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://agenticresourcediscovery.org/ref_implementations/
- group: other
  title: ''
  type: Adopters
  url: adoption/agentic-resource-discovery-adoption.yml
- group: other
  title: ''
  type: Adoption
  url: adoption/agentic-resource-discovery-adoption.yml
- group: other
  title: ''
  type: People
  url: people/agentic-resource-discovery-people.yml
- group: other
  title: ''
  type: Companies
  url: companies/agentic-resource-discovery-companies.yml
- group: other
  title: ''
  type: Leads
  url: leads/agentic-resource-discovery-new-company-leads.yml
- group: other
  title: ''
  type: Repositories
  url: repositories/agentic-resource-discovery-repositories.yml
- group: operate
  title: ''
  type: Releases
  url: releases/agentic-resource-discovery-releases.yml
- group: other
  title: ''
  type: Contributors
  url: contributors/agentic-resource-discovery-contributors.yml
- group: other
  title: ''
  type: WorkingGroups
  url: working-groups/agentic-resource-discovery-working-groups.yml
- group: other
  title: ''
  type: Taxonomy
  url: taxonomy/agentic-resource-discovery-taxonomy.yml
- group: other
  title: ''
  type: Glossary
  url: https://agenticresourcediscovery.org/glossary/
- group: operate
  title: ''
  type: FAQ
  url: https://agenticresourcediscovery.org/faq/
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticresourcediscovery.org/get_started/
created: 2026-05-19 00:00:00+00:00
description: 'Agentic Resource Discovery (ARD) is a proposed open standard for the discovery layer that sits in front of every agentic protocol — the step before invocation, where a client asks "what is available for this task?" and gets back a ranked set of MCP servers, agent cards, skills, workflows and APIs it could use. Publishers describe their resources once in an AI Catalog manifest at /.well-known/ai-catalog.json on their own domain, anchored by a urn:air: URN derived from that domain; independent discovery services crawl those manifests and expose them through a small REST interface whose only mandatory endpoint is POST /search. It deliberately does not execute anything — MCP, A2A and OpenAPI keep that job — and it deliberately does not try to be the one registry, inverting the submit-to-a-registry model in favour of publish-to-your-own-domain. Published as a v0.9 draft proposal on 28 May 2026 under Apache 2.0 by three authors at Microsoft, Google and Hugging Face, with a contributors
  wall of eleven organizations. It has no foundation, no charter, no participant roster and no working groups; it does have nine public architecture decision records and an official conformance CLI. This repo profiles it as a coalition with artifacts, and measures the distance between the specification and the endpoint.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentic-resource-discovery.png
json_schemas:
- name: AICatalogManifest
  property_count: 3
  slug: ai-catalog.schema
layout: provider
modified: 2026-07-31
name: Agentic Resource Discovery (ARD)
nav: Providers
network: true
overview: 'Agentic Resource Discovery (ARD) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agents API, Explore API, and Search API. Tagged areas include Agentic Resource Discovery, ARD, AI Catalog, Agent Discovery, and Discovery.


  Agentic Resource Discovery (ARD)''s developer surface includes FAQ, getting-started guide, and 26 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 75.0
  previous_composite: 31.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentic-resource-discovery/refs/heads/main/screenshots/agentic-resource-discovery-2026-08-07T161030.png
slug: agentic-resource-discovery
tags:
- Agentic Resource Discovery
- ARD
- AI Catalog
- Agent Discovery
- Discovery
- Well-Known URI
- Media Types
- Federation
- MCP
- A2A
- Agent Skills
- Standards
- Standards Body
- Specification
- Machine Readability
website: https://agenticresourcediscovery.org
---
