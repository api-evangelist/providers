---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Certificate Manager Agentic Access
  operation_count: 4
  slug: amazon-certificate-manager-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: Operations for requesting, describing, and managing SSL/TLS certificates
  name: Amazon Certificate Manager Certificates API
  slug: amazon-certificate-manager-certificates-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Certificate Manager Certificates API
  slug: open-amazon-certificate-manager-certificates-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-certificate-manager-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-certificate-manager-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-certificate-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-certificate-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-certificate-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-certificate-manager-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/certificate-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/acm/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/acm/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-certificate-manager
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/acm/latest/userguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-certificate-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-certificate-manager-vocabulary.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-certificate-manager-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-certificate-manager-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-certificate-manager-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-certificate-manager-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-certificate-manager-lifecycle.yml
created: '2024-01-15'
description: AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications, enabling you to manage certificate lifecycles centrally.
examples:
- key_count: 1
  name: Certificate Manager Describe Certificate Response Example
  slug: certificate-manager-describe-certificate-response-example
- key_count: 2
  name: Certificate Manager List Certificates Response Example
  slug: certificate-manager-list-certificates-response-example
- key_count: 4
  name: Certificate Manager Request Certificate Request Example
  slug: certificate-manager-request-certificate-request-example
- key_count: 1
  name: Certificate Manager Request Certificate Response Example
  slug: certificate-manager-request-certificate-response-example
features:
- description: Managed renewal for Amazon-issued SSL/TLS certificates, reducing manual maintenance overhead.
  name: Automated Certificate Renewal
- description: Provision both public certificates validated via DNS or email, and private certificates issued by a private CA.
  name: Public and Private Certificates
- description: Strong encryption and key management best practices for protecting and storing private keys.
  name: FIPS-Compliant Key Storage
- description: Deploy certificates to CloudFront, Elastic Load Balancing, API Gateway, and other integrated AWS services at no cost.
  name: Integrated AWS Service Deployment
- description: Provision and manage certificates for EC2, containers, on-premises hosts, and multicloud workloads.
  name: Hybrid and Multicloud Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-certificate-manager.png
integrations:
- description: Deploy ACM certificates to CloudFront distributions for HTTPS content delivery.
  name: Amazon CloudFront
- description: Attach ACM certificates to Application, Network, and Classic Load Balancers.
  name: Elastic Load Balancing
- description: Use ACM certificates for custom domain names in API Gateway.
  name: Amazon API Gateway
- description: Control access to ACM operations via IAM policies and roles.
  name: AWS IAM
- description: Audit all ACM API calls via CloudTrail for compliance and security monitoring.
  name: AWS CloudTrail
json_schemas:
- name: Amazon Certificate Manager Certificate
  property_count: 13
  slug: amazon-certificate-manager-certificate
- name: DescribeCertificateResponse
  property_count: 1
  slug: certificate-manager-describe-certificate-response
- name: ListCertificatesResponse
  property_count: 2
  slug: certificate-manager-list-certificates-response
- name: RequestCertificateRequest
  property_count: 4
  slug: certificate-manager-request-certificate-request
- name: RequestCertificateResponse
  property_count: 1
  slug: certificate-manager-request-certificate-response
json_structures:
- name: Certificate Manager Describe Certificate Response Structure
  property_count: 1
  slug: certificate-manager-describe-certificate-response-structure
- name: Certificate Manager List Certificates Response Structure
  property_count: 2
  slug: certificate-manager-list-certificates-response-structure
- name: Certificate Manager Request Certificate Request Structure
  property_count: 4
  slug: certificate-manager-request-certificate-request-structure
- name: Certificate Manager Request Certificate Response Structure
  property_count: 1
  slug: certificate-manager-request-certificate-response-structure
jsonld:
- class_count: 4
  name: Amazon Certificate Manager Context
  property_count: 8
  slug: amazon-certificate-manager-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Certificate Manager MCP Server
  slug: amazon-certificate-manager-mcp-server
modified: '2026-06-20'
name: Amazon Certificate Manager
nav: Providers
network: true
overview: 'Amazon Certificate Manager publishes 1 API on the [APIs.io](https://apis.io/) network: Certificates API. Tagged areas include Certificates, Encryption, Security, SSL, and TLS.


  The Amazon Certificate Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Certificate Manager''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 24 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Certificate Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-certificate-manager-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Amazon Certificate Manager API Rules
  rule_count: 32
  severity_counts:
    error: 15
    hint: 0
    info: 4
    warn: 13
  slug: amazon-certificate-manager-spectral-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 33.3
    contract_quality: 70.1
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 28.9
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/screenshots/amazon-certificate-manager-2026-07-25T195941.png
security:
- kind: domain-security
  name: Amazon Certificate Manager Domain Security
  slug: amazon-certificate-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Certificate Manager Vulnerability Disclosure
  slug: amazon-certificate-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Certificate Manager Trust Center
  slug: amazon-certificate-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-certificate-manager
tags:
- Certificates
- Encryption
- Security
- SSL
- TLS
use_cases:
- description: Securely terminate HTTPS traffic to public websites and web applications using ACM certificates.
  name: Website Protection
- description: Protect private network communication between servers, mobile devices, IoT devices, and internal applications.
  name: Internal Service Security
- description: Automated certificate lifecycle management prevents certificate expiration-related service downtime.
  name: Uptime Maintenance
- description: Centralize certificate management to meet compliance requirements and simplify security audits.
  name: Compliance and Audit
website: https://aws.amazon.com/certificate-manager/
---
