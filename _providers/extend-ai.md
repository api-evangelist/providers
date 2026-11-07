---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Extend Ai Agentic Access
  operation_count: 41
  slug: extend-ai-agentic-access
  summary_line: 41 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Classify API from Extend — 4 operation(s) for classify.
  name: Extend Classify API
  slug: extend-ai-classify-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Extract API from Extend — 6 operation(s) for extract.
  name: Extend Extract API
  slug: extend-ai-extract-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Files API from Extend — 3 operation(s) for files.
  name: Extend Files API
  slug: extend-ai-files-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Parse API from Extend — 3 operation(s) for parse.
  name: Extend Parse API
  slug: extend-ai-parse-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Split API from Extend — 3 operation(s) for split.
  name: Extend Split API
  slug: extend-ai-split-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Workflows API from Extend — 2 operation(s) for workflows.
  name: Extend Workflows API
  slug: extend-ai-workflows-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The API Reference API from Extend — 0 operation(s) for api reference.
  name: Extend API Reference API
  slug: extend-ai-api-reference-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The batchProcessorRun API from Extend — 1 operation(s) for batchprocessorrun.
  name: Extend Batch Processor Run API
  slug: extend-ai-batchprocessorrun-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The batchRuns API from Extend — 1 operation(s) for batchruns.
  name: Extend Batch Runs API
  slug: extend-ai-batchruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The classifiers API from Extend — 2 operation(s) for classifiers.
  name: Extend Classifiers API
  slug: extend-ai-classifiers-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The classifierVersions API from Extend — 2 operation(s) for classifierversions.
  name: Extend Classifier Versions API
  slug: extend-ai-classifierversions-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The classifyRuns API from Extend — 4 operation(s) for classifyruns.
  name: Extend Classify Runs API
  slug: extend-ai-classifyruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Detect Form API from Extend — 1 operation(s) for detect form.
  name: Extend Detect Form API
  slug: extend-ai-detect-form-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The Edit API from Extend — 1 operation(s) for edit.
  name: Extend Edit API
  slug: extend-ai-edit-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The editRuns API from Extend — 2 operation(s) for editruns.
  name: Extend Edit Runs API
  slug: extend-ai-editruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The editSchemas API from Extend — 1 operation(s) for editschemas.
  name: Extend Edit Schemas API
  slug: extend-ai-editschemas-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The editTemplates API from Extend — 2 operation(s) for edittemplates.
  name: Extend Edit Templates API
  slug: extend-ai-edittemplates-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The evaluationSetItems API from Extend — 2 operation(s) for evaluationsetitems.
  name: Extend Evaluation Set Items API
  slug: extend-ai-evaluationsetitems-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The evaluationSetRuns API from Extend — 2 operation(s) for evaluationsetruns.
  name: Extend Evaluation Set Runs API
  slug: extend-ai-evaluationsetruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The evaluationSets API from Extend — 2 operation(s) for evaluationsets.
  name: Extend Evaluation Sets API
  slug: extend-ai-evaluationsets-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The extractors API from Extend — 2 operation(s) for extractors.
  name: Extend Extractors API
  slug: extend-ai-extractors-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The extractorVersions API from Extend — 2 operation(s) for extractorversions.
  name: Extend Extractor Versions API
  slug: extend-ai-extractorversions-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The extractRuns API from Extend — 4 operation(s) for extractruns.
  name: Extend Extract Runs API
  slug: extend-ai-extractruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The formDetectionRuns API from Extend — 2 operation(s) for formdetectionruns.
  name: Extend Form Detection Runs API
  slug: extend-ai-formdetectionruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The parseRuns API from Extend — 4 operation(s) for parseruns.
  name: Extend Parse Runs API
  slug: extend-ai-parseruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The processor API from Extend — 2 operation(s) for processor.
  name: Extend Processor API
  slug: extend-ai-processor-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The processorRun API from Extend — 3 operation(s) for processorrun.
  name: Extend Processor Run API
  slug: extend-ai-processorrun-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The processorVersion API from Extend — 3 operation(s) for processorversion.
  name: Extend Processor Version API
  slug: extend-ai-processorversion-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The splitRuns API from Extend — 4 operation(s) for splitruns.
  name: Extend Split Runs API
  slug: extend-ai-splitruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The splitters API from Extend — 2 operation(s) for splitters.
  name: Extend Splitters API
  slug: extend-ai-splitters-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The splitterVersions API from Extend — 2 operation(s) for splitterversions.
  name: Extend Splitter Versions API
  slug: extend-ai-splitterversions-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The webhookEndpoints API from Extend — 2 operation(s) for webhookendpoints.
  name: Extend Webhook Endpoints API
  slug: extend-ai-webhookendpoints-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The webhookSubscriptions API from Extend — 2 operation(s) for webhooksubscriptions.
  name: Extend Webhook Subscriptions API
  slug: extend-ai-webhooksubscriptions-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The workflowRuns API from Extend — 4 operation(s) for workflowruns.
  name: Extend Workflow Runs API
  slug: extend-ai-workflowruns-api
- baseURL: https://api.extend.ai
  baseurl_source: declared
  description: The workflowVersions API from Extend — 2 operation(s) for workflowversions.
  name: Extend Workflow Versions API
  slug: extend-ai-workflowversions-api
artifact_total: 54
collections:
- collection_type: open
  name: Extend Batch API
  slug: open-extend-ai-batch-api
- collection_type: open
  name: Extend Batch Classify API
  slug: open-extend-ai-classify-api
- collection_type: open
  name: Extend Batch Evaluations API
  slug: open-extend-ai-evaluations-api
- collection_type: open
  name: Extend Batch Extract API
  slug: open-extend-ai-extract-api
- collection_type: open
  name: Extend Batch Files API
  slug: open-extend-ai-files-api
- collection_type: open
  name: Extend Batch Parse API
  slug: open-extend-ai-parse-api
- collection_type: open
  name: Extend Batch Split API
  slug: open-extend-ai-split-api
- collection_type: open
  name: Extend Batch Workflow Runs API
  slug: open-extend-ai-workflow-runs-api
- collection_type: open
  name: Extend Batch Workflows API
  slug: open-extend-ai-workflows-api
- collection_type: open
  name: Extend API
  slug: open-extend-ai
common:
- group: other
  href: https://artifacts.apis.io/extend-ai/capabilities/extend-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/extend-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/extend-ai/agentic-access/extend-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/extend-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/extend-ai/security/extend-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/extend-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/extend-ai/security/extend-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/extend-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/extend-ai/authentication/extend-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/extend-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extend-ai
- group: company
  title: ''
  type: Website
  url: https://www.extend.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.extend.ai
- group: commercial
  href: https://artifacts.apis.io/extend-ai/plans/extend-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/extend-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/extend-ai/rate-limits/extend-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/extend-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/extend-ai/finops/extend-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/extend-ai-finops.yml
created: '2026-06-20'
description: Extend is an intelligent document processing platform that turns documents into high quality, structured data. Its REST API at api.extend.ai exposes parsing, extraction, classification, and splitting processors, durable multi-step workflows, evaluation sets, and batch processing for automating document-heavy operations.
finops:
- has_sources: true
  method: generated
  name: Extend Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: extend-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extend-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.extend.ai over HTTP.
  name: Extend MCP Server
  slug: extend-ai
modified: '2026-06-20'
name: Extend
nav: Providers
network: true
overview: 'Extend publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Classify API, Extract API, Files API, and 32 more. Tagged areas include Document Processing, Document AI, Intelligent Document Processing, OCR, and Extraction.


  The Extend catalog on APIs.io includes 1 Spectral governance ruleset.


  Extend''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Extend Ai Plans Pricing
  plan_count: 3
  slug: extend-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Extend Ai Rate Limits
  slug: extend-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Extend API Rules
  rule_count: 57
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 12
  slug: extend-ai-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 56.2
    developer_ergonomics: 29.8
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.6
      total: 45
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/extend-ai/extend-ai-2026-06-20T180945.png
security:
- kind: authentication
  name: Extend Ai Authentication
  slug: extend-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Extend Ai Domain Security
  slug: extend-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Extend Ai Trust Center
  slug: extend-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: extend-ai
tags:
- Document Processing
- Document AI
- Intelligent Document Processing
- OCR
- Extraction
- Classification
website: https://www.extend.ai
---
