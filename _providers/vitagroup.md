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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-02'
api_count: 5
apis:
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: EHRbase's implementation of the official openEHR REST API (ITS-REST) — EHR, EHR_STATUS, COMPOSITION, DIRECTORY, CONTRIBUTION, versioned objects, ADL 1.4 / ADL 2 template definitions and Archetype Quer
  name: HIP EHRbase openEHR REST API
  slug: hip-ehrbase-openehr
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: EHRbase's non-standard administrative API — hard delete and update of EHRs, compositions, contributions, directories, stored queries and templates, plus the HIP EHRbase Merge EHR operations (merge, me
  name: HIP EHRbase Admin API
  slug: hip-ehrbase-admin
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: Experimental EHRbase API for attaching, reading and deleting ITEM_TAG key/value annotations on EHR_STATUS and COMPOSITION versioned objects, addressed by openEHR path. 2 paths / 6 operations. Marked e
  name: HIP EHRbase Item Tag Experimental API
  slug: hip-ehrbase-item-tags
- baseURL: https://{ehrbaseBaseUrl}
  baseurl_source: declared
  description: The closed-source HIP EHRbase enterprise plugin API — Event Trigger management (AQL-defined hooks that forward composition and EHR_STATUS events over HTTP, AMQP/RabbitMQ or Kafka), Multi-tenant provis
  name: HIP EHRbase Enterprise API
  slug: hip-ehrbase-enterprise
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The OpenAPI document served by vitagroup's public EHRbase sandbox instance at sandkiste.ehrbase.org, harvested from /ehrbase/v3/api-docs. Combines the openEHR, EHR-Scape (ECIS), Admin and Status surfa
  name: EHRbase Sandbox (live springdoc api-docs)
  slug: ehrbase-sandbox-live
artifact_total: 13
asyncapis:
- description: ''
  name: Vitagroup Event Trigger Webhooks
  slug: vitagroup-event-trigger-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.vitagroup.ag/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ehrbase.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ehrbase.org/docs/EHRbase/openEHR-Introduction/Introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ehrbase.org/api/hip-ehrbase/openehr
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ehrbase.org/docs/EHRbase/Installation
- group: start
  title: ''
  type: Sandbox
  url: https://sandkiste.ehrbase.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vitagroupag
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ehrbase/ehrbase
- group: operate
  title: ''
  type: Support
  url: https://hip.vitagroup.ag/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://hip.vitagroup.ag/en/tech-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hip.vitagroup.ag/en/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vitagroup.ag/en/privacy/
- group: other
  title: ''
  type: Imprint
  url: https://www.vitagroup.ag/en/imprint/
- group: start
  title: ''
  type: SignUp
  url: https://hip.vitagroup.ag/en/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vitagroup-ag/
- group: build
  title: ''
  type: Packages
  url: packages/vitagroup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vitagroup-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vitagroup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vitagroup-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vitagroup-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vitagroup-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vitagroup-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/vitagroup-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vitagroup-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vitagroup-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vitagroup-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vitagroup-event-trigger-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vitagroup-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vitagroup-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vitagroup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vitagroup-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitagroup-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/vitagroup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vitagroup-vulnerability-disclosure.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vitagroup-hip-ehrbase-openehr-overlay.yaml
created: '2026-09-02'
description: vitagroup AG is a German health-technology company (Mannheim, HRB 727147) that builds the Health Intelligence Platform (HIP) — an open, vendor-neutral clinical data platform for hospitals, health regions and research institutions. HIP is built on the openEHR standard and its Clinical Data Repository is HIP EHRbase, the commercially supported distribution of EHRbase, the leading open-source openEHR server. vitagroup operates the EHRbase project (ehrbase.org names vitagroup AG as the responsible entity), publishes the openEHR REST, Admin, Item Tag and HIP Enterprise OpenAPI definitions at docs.ehrbase.org, and runs a public unauthenticated sandbox instance at sandkiste.ehrbase.org. FHIR and HL7v2 interoperability is provided through the CDR Bridge / FHIR Bridge and the openFHIR and FHIRconnect projects.
image: https://www.vitagroup.ag/wp-content/uploads/2023/09/vitagroup_Vorschau_berry_4zu3-1024x819.png
layout: provider
mcp_servers:
- description: ''
  name: vitagroup MCP Server
  slug: vitagroup-mcp-server
modified: '2026-09-02'
name: vitagroup
nav: Providers
network: true
overview: 'vitagroup publishes 5 APIs on the [APIs.io](https://apis.io/) network, including HIP EHRbase openEHR REST API, HIP EHRbase Admin API, HIP EHRbase Item Tag Experimental API, and 2 more. Tagged areas include Company, Healthcare, Health IT, Electronic Health Records, and openEHR.


  The vitagroup catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  vitagroup''s developer surface includes documentation, API reference, getting-started guide, sandbox, support, engineering blog, signup flow, and 29 more developer resources.'
plans:
- name: Vitagroup Plans Pricing
  plan_count: 0
  slug: vitagroup-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Vitagroup Rate Limits
  slug: vitagroup-rate-limits
scopes:
- name: Vitagroup Scopes
  scope_count: 0
  slug: vitagroup-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 46.1
    developer_ergonomics: 73.2
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Vitagroup Authentication
  slug: vitagroup-authentication
  summary_line: none/http/oauth2 · 0 schemes
- kind: domain-security
  name: Vitagroup Domain Security
  slug: vitagroup-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Vitagroup Vulnerability Disclosure
  slug: vitagroup-vulnerability-disclosure
  summary_line: disclosure policy published
slug: vitagroup
tags:
- Company
- Healthcare
- Health IT
- Electronic Health Records
- openEHR
- FHIR
- Clinical Data Repository
- Interoperability
- Germany
- Open Source
website: https://www.vitagroup.ag/
---
