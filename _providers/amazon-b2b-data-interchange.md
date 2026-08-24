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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Amazon B2B Data Interchange Agentic Access
  operation_count: 30
  slug: amazon-b2b-data-interchange-agentic-access
  summary_line: 30 operations · 20 acting
api_count: 6
apis:
- description: Manage EDI transformation capabilities
  name: Amazon B2B Data Interchange Capabilities API
  slug: amazon-b2b-data-interchange-capabilities-api
- description: Manage partnerships between customers and trading partners
  name: Amazon B2B Data Interchange Partnerships API
  slug: amazon-b2b-data-interchange-partnerships-api
- description: Manage customer profiles representing private networks
  name: Amazon B2B Data Interchange Profiles API
  slug: amazon-b2b-data-interchange-profiles-api
- description: Manage resource tags
  name: Amazon B2B Data Interchange Tags API
  slug: amazon-b2b-data-interchange-tags-api
- description: Test and validate mappings, parsing, and conversions
  name: Amazon B2B Data Interchange Testing API
  slug: amazon-b2b-data-interchange-testing-api
- description: Manage EDI transformers for document conversion
  name: Amazon B2B Data Interchange Transformers API
  slug: amazon-b2b-data-interchange-transformers-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS B2B Data Interchange Capabilities API
  slug: open-amazon-b2b-data-interchange-capabilities-api
- collection_type: open
  name: AWS B2B Data Interchange Capabilities Partnerships API
  slug: open-amazon-b2b-data-interchange-partnerships-api
- collection_type: open
  name: AWS B2B Data Interchange Capabilities Profiles API
  slug: open-amazon-b2b-data-interchange-profiles-api
- collection_type: open
  name: AWS B2B Data Interchange Capabilities Tags API
  slug: open-amazon-b2b-data-interchange-tags-api
- collection_type: open
  name: AWS B2B Data Interchange Capabilities Testing API
  slug: open-amazon-b2b-data-interchange-testing-api
- collection_type: open
  name: AWS B2B Data Interchange Capabilities Transformers API
  slug: open-amazon-b2b-data-interchange-transformers-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-b2b-data-interchange-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-b2b-data-interchange-aws-b2b-data-interchange-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-b2b-data-interchange-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-b2b-data-interchange-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-b2b-data-interchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-b2b-data-interchange-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-b2b-data-interchange-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-b2b-data-interchange-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-b2b-data-interchange-llms.txt
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/b2bi/
- group: build
  title: ''
  type: SDK
  url: https://github.com/aws/aws-sdk-js-v3/tree/main/clients/client-b2bi
- group: build
  title: ''
  type: SDK
  url: https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/b2bi
- group: build
  title: ''
  type: SDK
  url: https://docs.rs/aws-sdk-b2bi
- group: build
  title: ''
  type: Samples
  url: https://github.com/aws-samples/aws-b2b-data-interchange-toolkit
- group: other
  title: ''
  type: CloudFormation
  url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_B2BI.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/b2b-data-interchange/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
created: '2026-03-16'
description: AWS B2B Data Interchange is a fully managed service that automates the transformation and exchange of electronic data interchange (EDI) documents at cloud scale. It enables businesses to onboard trading partners, transform X12 EDI documents to and from JSON or XML, and manage capabilities, profiles, and partnerships with pay-as-you-go pricing. The service supports supply chain, healthcare, and financial services workflows and leverages Amazon Bedrock for AI-assisted mapping generation.
examples:
- key_count: 2
  name: Create Capability Example
  slug: create-capability-example
- key_count: 2
  name: Create Partnership Example
  slug: create-partnership-example
- key_count: 2
  name: Create Profile Example
  slug: create-profile-example
- key_count: 2
  name: Create Transformer Example
  slug: create-transformer-example
- key_count: 2
  name: Generate Mapping Example
  slug: generate-mapping-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-b2b-data-interchange.png
json_schemas:
- name: Partnership
  property_count: 10
  slug: partnership
- name: Profile
  property_count: 10
  slug: profile
- name: Transformer
  property_count: 9
  slug: transformer
json_structures:
- name: B2Bi Resource Structure
  property_count: 0
  slug: b2bi-resource-structure
jsonld:
- class_count: 36
  name: context Context
  property_count: 2
  slug: context
layout: provider
mcp_servers:
- description: ''
  name: Amazon B2B Data Interchange MCP Server
  slug: amazon-b2b-data-interchange-mcp-server
modified: '2026-06-20'
name: Amazon B2B Data Interchange
nav: Providers
network: true
overview: 'Amazon B2B Data Interchange publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Capabilities API, Partnerships API, Profiles API, and 3 more. Tagged areas include EDI, B2B, Data Interchange, Supply Chain, and Healthcare.


  The Amazon B2B Data Interchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon B2B Data Interchange''s developer surface includes authentication, CLI, SDKs, pricing, and 14 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon B2B Data Interchange API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-b2b-data-interchange-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 26.5
    contract_quality: 77.3
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 26.5
    operational_transparency: 0.0
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-b2b-data-interchange/refs/heads/main/screenshots/amazon-b2b-data-interchange-2026-07-25T195932.png
security:
- kind: authentication
  name: Amazon B2B Data Interchange Authentication
  slug: amazon-b2b-data-interchange-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon B2B Data Interchange Domain Security
  slug: amazon-b2b-data-interchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon B2B Data Interchange Vulnerability Disclosure
  slug: amazon-b2b-data-interchange-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-b2b-data-interchange
tags:
- EDI
- B2B
- Data Interchange
- Supply Chain
- Healthcare
- Financial-Services
- Amazon Web Services
---
