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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Braket Agentic Access
  operation_count: 17
  slug: amazon-braket-agentic-access
  summary_line: 17 operations · 13 acting
api_count: 5
apis:
- description: Discover and retrieve details about quantum devices
  name: Amazon Braket Devices API
  slug: amazon-braket-devices-api
- description: Manage hybrid quantum-classical jobs
  name: Amazon Braket Jobs API
  slug: amazon-braket-jobs-api
- description: Submit and manage quantum tasks on QPUs and simulators
  name: Amazon Braket Quantum Tasks API
  slug: amazon-braket-quantum-tasks-api
- description: Control QPU and simulator spending
  name: Amazon Braket Spending Limits API
  slug: amazon-braket-spending-limits-api
- description: Manage resource tags
  name: Amazon Braket Tags API
  slug: amazon-braket-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Braket Devices API
  slug: open-amazon-braket-devices-api
- collection_type: open
  name: Amazon Braket Devices Jobs API
  slug: open-amazon-braket-jobs-api
- collection_type: open
  name: Amazon Braket Devices Quantum Tasks API
  slug: open-amazon-braket-quantum-tasks-api
- collection_type: open
  name: Amazon Braket Devices Spending Limits API
  slug: open-amazon-braket-spending-limits-api
- collection_type: open
  name: Amazon Braket Devices Tags API
  slug: open-amazon-braket-tags-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-braket-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-braket-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-braket-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-braket-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-braket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-braket-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-braket-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/braket/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/braket/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/braket/faqs/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/braket/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/quantum-computing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amazon-braket
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/braket/
- group: build
  title: ''
  type: SDK
  url: https://github.com/amazon-braket/amazon-braket-sdk-python
- group: build
  title: ''
  type: Examples
  url: https://github.com/amazon-braket/amazon-braket-examples
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: build
  title: ''
  type: Packages
  url: packages/amazon-braket-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-braket-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-braket-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-braket-llms.txt
created: '2026-03-16'
description: Amazon Braket is a fully managed quantum computing service that helps researchers and developers explore and build quantum algorithms, test them on quantum circuit simulators, and run them on different quantum hardware technologies. Braket provides access to multiple quantum processors from IonQ, Rigetti, QuEra, Oxford Quantum Circuits, and IQM, as well as high-performance quantum circuit simulators. It supports hybrid quantum-classical algorithms through Braket Hybrid Jobs.
examples:
- key_count: 2
  name: Create Hybrid Job Example
  slug: create-hybrid-job-example
- key_count: 2
  name: Create Quantum Task Example
  slug: create-quantum-task-example
- key_count: 2
  name: Search Devices Example
  slug: search-devices-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-braket.png
json_schemas:
- name: Quantum Task
  property_count: 10
  slug: braket-task
json_structures:
- name: Braket Resource Structure
  property_count: 0
  slug: braket-resource-structure
jsonld:
- class_count: 23
  name: context Context
  property_count: 3
  slug: context
layout: provider
mcp_servers:
- description: ''
  name: amazon-braket-mcp.yml
  slug: amazon-braket-mcpyml
modified: '2026-06-20'
name: Amazon Braket
nav: Providers
network: true
overview: 'Amazon Braket publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Jobs API, Quantum Tasks API, and 2 more. Tagged areas include Quantum Computing, Quantum Hardware, Hybrid Quantum-Classical, QPU, and Quantum Simulation.


  The Amazon Braket catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Braket''s developer surface includes authentication, developer portal, documentation, pricing, FAQ, getting-started guide, engineering blog, and 18 more developer resources.'
random_paper: 132
rules:
- name: Amazon Braket API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-braket-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.5
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 69.8
    operational_transparency: 5.3
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-braket/refs/heads/main/screenshots/amazon-braket-2026-07-25T195944.png
security:
- kind: authentication
  name: Amazon Braket Authentication
  slug: amazon-braket-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Braket Domain Security
  slug: amazon-braket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Braket Vulnerability Disclosure
  slug: amazon-braket-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Braket Trust Center
  slug: amazon-braket-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-braket
tags:
- Quantum Computing
- Quantum Hardware
- Hybrid Quantum-Classical
- QPU
- Quantum Simulation
- Amazon Web Services
- Research
- HPC
website: https://aws.amazon.com/braket/
---
