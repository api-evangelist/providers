---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Fraud Detector Agentic Access
  operation_count: 13
  slug: amazon-fraud-detector-agentic-access
  summary_line: 13 operations · 12 acting
api_count: 1
apis:
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Fraud detector configurations
  name: Amazon Fraud Detector Detectors API
  slug: amazon-fraud-detector-detectors-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Event schema definitions
  name: Amazon Fraud Detector Event Types API
  slug: amazon-fraud-detector-event-types-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Fraud and legitimate transaction labels
  name: Amazon Fraud Detector Labels API
  slug: amazon-fraud-detector-labels-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: ML model training and versioning
  name: Amazon Fraud Detector Models API
  slug: amazon-fraud-detector-models-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Real-time fraud prediction
  name: Amazon Fraud Detector Predictions API
  slug: amazon-fraud-detector-predictions-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Business logic rules for fraud decisions
  name: Amazon Fraud Detector Rules API
  slug: amazon-fraud-detector-rules-api
- baseURL: https://frauddetector.amazonaws.com
  baseurl_source: declared
  description: Resource metadata labels
  name: Amazon Fraud Detector Tags API
  slug: amazon-fraud-detector-tags-api
arazzos:
- description: Create a DETECTORPL rule for a detector and read the detector's rules back to confirm it.
  name: Amazon Fraud Detector Author Rule
  slug: amazon-fraud-detector-author-rule-workflow
- description: Create fraud and legit labels, define an event type that uses them, then confirm the event type exists.
  name: Amazon Fraud Detector Bootstrap Event Type
  slug: amazon-fraud-detector-bootstrap-event-type-workflow
- description: Inspect a detector's rules and then delete the detector, branching when rules still block deletion.
  name: Amazon Fraud Detector Decommission Detector
  slug: amazon-fraud-detector-decommission-detector-workflow
- description: Define an event type, create a detector and a rule, then score a sample event against the detector.
  name: Amazon Fraud Detector Detector Pipeline
  slug: amazon-fraud-detector-detector-pipeline-workflow
- description: List models for an event type, then list detectors and tag a chosen detector with its model count.
  name: Amazon Fraud Detector Inventory Models and Detectors
  slug: amazon-fraud-detector-inventory-models-detectors-workflow
- description: Define an event type, create an ML model and a detector on top of it, then confirm the detector exists.
  name: Amazon Fraud Detector Provision Model and Detector
  slug: amazon-fraud-detector-provision-model-detector-workflow
- description: Score an event against a detector and branch on the returned model score to tag the detector accordingly.
  name: Amazon Fraud Detector Score Event and Tag
  slug: amazon-fraud-detector-score-event-and-tag-workflow
- description: Assign tags to a Fraud Detector resource and read its tags back to confirm they were applied.
  name: Amazon Fraud Detector Tag and Audit Resource
  slug: amazon-fraud-detector-tag-and-audit-resource-workflow
artifact_total: 64
collections:
- collection_type: postman
  name: Amazon Fraud Detector API
  slug: postman-amazon-fraud-detector
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Fraud Detector Detectors API
  slug: open-amazon-fraud-detector-detectors-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Event Types API
  slug: open-amazon-fraud-detector-event-types-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Labels API
  slug: open-amazon-fraud-detector-labels-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Models API
  slug: open-amazon-fraud-detector-models-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Predictions API
  slug: open-amazon-fraud-detector-predictions-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Rules API
  slug: open-amazon-fraud-detector-rules-api
- collection_type: open
  name: Amazon Fraud Detector Detectors Tags API
  slug: open-amazon-fraud-detector-tags-api
- collection_type: open
  name: Amazon Fraud Detector API
  slug: open-amazon-fraud-detector
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-fraud-detector-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-fraud-detector-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-fraud-detector-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-fraud-detector-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-fraud-detector-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-fraud-detector-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-fraud-detector/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-author-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-bootstrap-event-type-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-decommission-detector-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-detector-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-inventory-models-detectors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-provision-model-detector-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-score-event-and-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fraud-detector-tag-and-audit-resource-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/fraud-detector/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/fraud-detector/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/frauddetector/
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
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/frauddetector/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-fraud-detector
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-fraud-detector-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-fraud-detector-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-fraud-detector-context.jsonld
created: '2026-03-16'
description: Amazon Fraud Detector is a fully managed service that uses machine learning to identify potentially fraudulent activities and accurately distinguish between legitimate and high-risk transactions. It uses your data and the same technology that Amazon uses to protect its own business from fraud.
examples:
- key_count: 6
  name: Amazon Fraud Detector Detector Example
  slug: amazon-fraud-detector-detector-example
- key_count: 7
  name: Amazon Fraud Detector Event Type Example
  slug: amazon-fraud-detector-event-type-example
- key_count: 7
  name: Amazon Fraud Detector Model Example
  slug: amazon-fraud-detector-model-example
- key_count: 8
  name: Amazon Fraud Detector Rule Example
  slug: amazon-fraud-detector-rule-example
- key_count: 2
  name: Amazon Fraud Detector Tag Example
  slug: amazon-fraud-detector-tag-example
features:
- description: Automatically trains and deploys ML models using your historical transaction data without requiring ML expertise.
  name: No ML Expertise Required
- description: Returns fraud scores within milliseconds for integration into transaction approval flows.
  name: Real-Time Fraud Scoring
- description: Online Fraud Insights (OFI), Transaction Fraud Insights (TFI), and Account Takeover Insights (ATI) pre-trained model types.
  name: Pre-Built Models
- description: DETECTORPL rule language allows writing conditional logic using model scores and event variables.
  name: Rule Engine
- description: Variable importance scores explain which factors most influenced a fraud prediction.
  name: Model Explainability
- description: Uses Amazon fraud experience to provide immediate predictions even with limited historical data.
  name: Cold Start Protection
- description: Ingest historical labeled events to continuously improve model accuracy over time.
  name: Event Ingestion
finops:
- name: Amazon Fraud Detector Finops
  service_category: API
  slug: amazon-fraud-detector-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-fraud-detector.png
json_schemas:
- name: Detector
  property_count: 6
  slug: amazon-fraud-detector-detector
- name: EventType
  property_count: 7
  slug: amazon-fraud-detector-event-type
- name: Model
  property_count: 7
  slug: amazon-fraud-detector-model
- name: Rule
  property_count: 8
  slug: amazon-fraud-detector-rule
- name: Tag
  property_count: 2
  slug: amazon-fraud-detector-tag
json_structures:
- name: Amazon Fraud Detector Detector Structure
  property_count: 0
  slug: amazon-fraud-detector-detector-structure
- name: Amazon Fraud Detector Event Type Structure
  property_count: 0
  slug: amazon-fraud-detector-event-type-structure
- name: Amazon Fraud Detector Model Structure
  property_count: 0
  slug: amazon-fraud-detector-model-structure
- name: Amazon Fraud Detector Rule Structure
  property_count: 0
  slug: amazon-fraud-detector-rule-structure
- name: Amazon Fraud Detector Tag Structure
  property_count: 0
  slug: amazon-fraud-detector-tag-structure
jsonld:
- class_count: 5
  name: Amazon Fraud Detector Context
  property_count: 12
  slug: amazon-fraud-detector-context
layout: provider
modified: '2026-05-19'
name: Amazon Fraud Detector
nav: Providers
network: true
overview: 'Amazon Fraud Detector publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Detectors API, Event Types API, Labels API, and 4 more. Tagged areas include Financial-Services, Fraud Detection, Machine-Learning, and Security.


  The Amazon Fraud Detector catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Fraud Detector''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 24 more developer resources.'
plans:
- name: Amazon Fraud Detector Plans Pricing
  plan_count: 3
  slug: amazon-fraud-detector-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Amazon Fraud Detector Rate Limits
  slug: amazon-fraud-detector-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Fraud Detector API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-fraud-detector-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: Amazon Fraud Detector API Rules
  rule_count: 35
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 25
  slug: amazon-fraud-detector-spectral-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 75.9
    developer_ergonomics: 57.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/screenshots/amazon-fraud-detector-2026-06-20T171653.png
security:
- kind: authentication
  name: Amazon Fraud Detector Authentication
  slug: amazon-fraud-detector-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Fraud Detector Domain Security
  slug: amazon-fraud-detector-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Fraud Detector Vulnerability Disclosure
  slug: amazon-fraud-detector-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Fraud Detector Trust Center
  slug: amazon-fraud-detector-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-fraud-detector
tags:
- Financial-Services
- Fraud Detection
- Machine-Learning
- Security
use_cases:
- description: Score credit card and payment transactions in real-time to block fraudulent purchases.
  name: Payment Fraud Detection
- description: Detect unauthorized login attempts and account compromise using behavioral signals.
  name: Account Takeover Prevention
- description: Identify fraudulent new account registrations at signup to prevent synthetic identity fraud.
  name: New Account Fraud
- description: Flag users abusing discount codes, referral bonuses, and promotional offers.
  name: Promotion Abuse Detection
- description: Reduce chargeback rates by blocking high-risk transactions before they complete.
  name: Chargeback Prevention
- description: Score insurance claims for fraudulent patterns in real-time during claim submission.
  name: Insurance Claims Fraud
website: https://aws.amazon.com/fraud-detector/
---
