---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Certificate Manager Agentic Access
  operation_count: 4
  slug: amazon-certificate-manager-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: Operations for requesting, describing, and managing SSL/TLS certificates
  name: Amazon Certificate Manager Certificates API
  slug: amazon-certificate-manager-certificates-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Acme Account API from Amazon Certificate Manager — 3 operation(s) for certificate manager acme account.
  name: Amazon Certificate Manager Certificate Manager Acme Account API
  slug: amazon-certificate-manager-acme-account-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Acme Domain Validation API from Amazon Certificate Manager — 5 operation(s) for certificate manager acme domain validation.
  name: Amazon Certificate Manager Certificate Manager Acme Domain Validation API
  slug: amazon-certificate-manager-acme-domain-validation-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Acme Endpoint API from Amazon Certificate Manager — 5 operation(s) for certificate manager acme endpoint.
  name: Amazon Certificate Manager Certificate Manager Acme Endpoint API
  slug: amazon-certificate-manager-acme-endpoint-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Acme External Account Binding API from Amazon Certificate Manager — 5 operation(s) for certificate manager acme external account binding.
  name: Amazon Certificate Manager Certificate Manager Acme External Account Binding API
  slug: amazon-certificate-manager-acme-external-account-binding-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Operations API from Amazon Certificate Manager — 9 operation(s) for certificate manager operations.
  name: Amazon Certificate Manager Certificate Manager Operations API
  slug: amazon-certificate-manager-operations-api
- baseURL: https://acm.amazonaws.com
  baseurl_source: declared
  description: The Certificate Manager Tag API from Amazon Certificate Manager — 4 operation(s) for certificate manager tag.
  name: Amazon Certificate Manager Certificate Manager Tag API
  slug: amazon-certificate-manager-tag-api
artifact_total: 44
collections:
- collection_type: open
  name: Amazon Certificate Manager Certificates API
  slug: open-amazon-certificate-manager-certificates-api
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-certificate-manager/plans/amazon-certificate-manager-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-certificate-manager-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-certificate-manager/overview
- group: other
  href: https://artifacts.apis.io/amazon-certificate-manager/capabilities/amazon-certificate-manager-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-certificate-manager-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/amazon-certificate-manager/mcp/amazon-certificate-manager-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazon-certificate-manager-mcp.yml
- group: other
  href: https://artifacts.apis.io/amazon-certificate-manager/overlays/amazon-certificate-manager-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazon-certificate-manager-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/amazon-certificate-manager/agentic-access/amazon-certificate-manager-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-certificate-manager-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-certificate-manager/security/amazon-certificate-manager-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-certificate-manager-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-certificate-manager/security/amazon-certificate-manager-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-certificate-manager-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-certificate-manager/security/amazon-certificate-manager-domain-security.yml
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
  href: https://artifacts.apis.io/amazon-certificate-manager/rules/amazon-certificate-manager-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-certificate-manager-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-certificate-manager/vocabulary/amazon-certificate-manager-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-certificate-manager-vocabulary.yaml
- group: agent
  href: https://artifacts.apis.io/amazon-certificate-manager/well-known/amazon-certificate-manager-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-certificate-manager-well-known.yml
- group: auth
  href: https://artifacts.apis.io/amazon-certificate-manager/well-known/amazon-certificate-manager-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-certificate-manager-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-certificate-manager/llms/amazon-certificate-manager-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-certificate-manager-llms.txt
- group: design
  href: https://artifacts.apis.io/amazon-certificate-manager/conformance/amazon-certificate-manager-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-certificate-manager-conformance.yml
- group: design
  href: https://artifacts.apis.io/amazon-certificate-manager/lifecycle/amazon-certificate-manager-lifecycle.yml
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
finops:
- has_sources: true
  method: derived
  name: Amazon Certificate Manager Finops
  primary_unit: domain
  service_category: ''
  slug: amazon-certificate-manager-finops
  template: false
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
modified: '2026-06-20'
name: Amazon Certificate Manager
nav: Providers
network: true
overview: 'Amazon Certificate Manager publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Certificates API, Certificate Manager Acme Account API, Certificate Manager Acme Domain Validation API, and 4 more. Tagged areas include Amazon Web Services, Certificates, Encryption, Security, and SSL.


  The Amazon Certificate Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Certificate Manager''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 27 more developer resources.'
plans:
- name: Amazon Certificate Manager Plans Pricing
  plan_count: 12
  slug: amazon-certificate-manager-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon Certificate Manager — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-certificate-manager-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 73
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
  composite: 66.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 75.0
    catalog_earned_first_party: 12.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 71.3
    developer_ergonomics: 60.7
    discoverability: 73.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.7
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-certificate-manager/amazon-certificate-manager-2026-07-25T195941.png
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
- Amazon Web Services
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
