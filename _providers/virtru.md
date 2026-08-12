---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 116
  human_in_the_loop: 0
  name: Virtru Agentic Access
  operation_count: 116
  slug: virtru-agentic-access
  summary_line: 116 operations · 116 acting
api_count: 14
apis:
- description: The authorization.AuthorizationService API from Virtru — 3 operation(s) for authorization.authorizationservice.
  name: Virtru authorization.AuthorizationService API
  slug: virtru-authorization-authorizationservice-api
- description: The authorization.v2.AuthorizationService API from Virtru — 4 operation(s) for authorization.v2.authorizationservice.
  name: Virtru authorization.v2.AuthorizationService API
  slug: virtru-authorization-v2-authorizationservice-api
- description: The entityresolution.v2.EntityResolutionService API from Virtru — 2 operation(s) for entityresolution.v2.entityresolutionservice.
  name: Virtru entityresolution.v2.EntityResolutionService API
  slug: virtru-entityresolution-v2-entityresolutionservice-api
- description: Get app info from the root path
  name: Virtru kas.AccessService API
  slug: virtru-kas-accessservice-api
- description: The policy.actions.ActionService API from Virtru — 5 operation(s) for policy.actions.actionservice.
  name: Virtru policy.actions.ActionService API
  slug: virtru-policy-actions-actionservice-api
- description: / / Attribute Service /
  name: Virtru policy.attributes.AttributesService API
  slug: virtru-policy-attributes-attributesservice-api
- description: The policy.kasregistry.KeyAccessServerRegistryService API from Virtru — 14 operation(s) for policy.kasregistry.keyaccessserverregistryservice.
  name: Virtru policy.kasregistry.KeyAccessServerRegistryService API
  slug: virtru-policy-kasregistry-keyaccessserverregistryservice-api
- description: The policy.keymanagement.KeyManagementService API from Virtru — 5 operation(s) for policy.keymanagement.keymanagementservice.
  name: Virtru policy.keymanagement.KeyManagementService API
  slug: virtru-policy-keymanagement-keymanagementservice-api
- description: The policy.namespaces.NamespaceService API from Virtru — 9 operation(s) for policy.namespaces.namespaceservice.
  name: Virtru policy.namespaces.NamespaceService API
  slug: virtru-policy-namespaces-namespaceservice-api
- description: / / Obligation Service /
  name: Virtru policy.obligations.Service API
  slug: virtru-policy-obligations-service-api
- description: Registered Resources
  name: Virtru policy.registeredresources.RegisteredResourcesService API
  slug: virtru-policy-registeredresources-registeredresourcesservice-api
- description: Resource Mapping Groups
  name: Virtru policy.resourcemapping.ResourceMappingService API
  slug: virtru-policy-resourcemapping-resourcemappingservice-api
- description: The policy.subjectmapping.SubjectMappingService API from Virtru — 12 operation(s) for policy.subjectmapping.subjectmappingservice.
  name: Virtru policy.subjectmapping.SubjectMappingService API
  slug: virtru-policy-subjectmapping-subjectmappingservice-api
- description: The wellknownconfiguration.WellKnownService API from Virtru — 1 operation(s) for wellknownconfiguration.wellknownservice.
  name: Virtru wellknownconfiguration.WellKnownService API
  slug: virtru-wellknownconfiguration-wellknownservice-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.virtru.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.virtru.com/developers/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://opentdf.io
- group: docs
  title: ''
  type: APIReference
  url: https://opentdf.io/OpenAPI-clients
- group: start
  title: ''
  type: GettingStarted
  url: https://opentdf.io/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentdf
- group: company
  title: ''
  type: Blog
  url: https://www.virtru.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.virtru.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtru.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtru.com/terms-of-service
- group: build
  title: ''
  type: Packages
  url: packages/virtru-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virtru-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/virtru-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtru-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtru-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtru-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtru-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/virtru-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtru-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtru-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtru-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.virtru.com/
- group: other
  title: ''
  type: Protobuf
  url: grpc/virtru-kas.proto
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtru-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtru-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/virtru-kas-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/virtru-policy-attributes-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virtru-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virtru-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/virtru-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/virtru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.virtru.com/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtru-domain-security.yml
created: '2026-07-17'
description: Virtru is a data-centric security company whose Data Security Platform is built on OpenTDF, the open Trusted Data Format. Applications encrypt data with attribute-based access control (ABAC) and enforce who can decrypt it through Key Access Servers (KAS), independent of where the data travels — email, files, SaaS, and data pipelines. The platform exposes Connect-protocol (gRPC + HTTP/JSON) services for policy (namespaces, attributes, values, subject mappings), key access, authorization decisions, and entity resolution, authenticated with OIDC/OAuth 2.0. Virtru maintains the open-source OpenTDF project and ships SDKs for JavaScript, Go, and Java plus the otdfctl CLI. Backed by Bessemer Venture Partners and ICONIQ Capital.
image: https://www.virtru.com/hubfs/assets/images/logos/virtru/logomark/blue/virtru_LOGOMARKMASTER_BLUE_FINAL.png
layout: provider
mcp_servers:
- description: ''
  name: virtru-mcp.yml
  slug: virtru-mcpyml
modified: '2026-07-21'
name: Virtru
nav: Providers
network: true
overview: 'Virtru publishes 14 APIs on the [APIs.io](https://apis.io/) network, including authorization.AuthorizationService API, authorization.v2.AuthorizationService API, entityresolution.v2.EntityResolutionService API, and 11 more. Tagged areas include Company, Cybersecurity, Data Security, Encryption, and Access Control.


  Virtru''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, CLI, authentication, and 27 more developer resources.'
random_paper: 104
score:
  band: developing
  composite: 48.5
  delta: -1.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 41.0
    developer_ergonomics: 64.7
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Virtru Authentication
  slug: virtru-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Virtru Domain Security
  slug: virtru-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Virtru Vulnerability Disclosure
  slug: virtru-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Virtru Trust Center
  slug: virtru-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, FedRAMP, FIPS 140
slug: virtru
tags:
- Company
- Cybersecurity
- Data Security
- Encryption
- Access Control
- Zero Trust
- Data Privacy
- OpenTDF
- Key Management
website: https://www.virtru.com/
---
