---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: Performs detailed multilingual sentiment analysis of texts from different sources, returning polarity, agreement, subjectivity, irony, and confidence scores at document, sentence, and segment levels.
  name: Sentiment Analysis API
  slug: sentiment-analysis-api
- description: Identifies and extracts named entities (people, places, organizations) and abstract concepts within text, providing relevance scores and ontology types.
  name: Topics Extraction API
  slug: topics-extraction-api
- description: Assigns one or more classes to a text according to content using predefined or custom taxonomy models, supporting multilingual classification with configurable hierarchy expansion.
  name: Text Classification API
  slug: text-classification-api
- description: Detects the language in which a given text is written, returning ISO-639 codes and confidence scores for multiple candidate languages.
  name: Language Identification API
  slug: language-identification-api
- description: Premium API that performs deep semantic text classification using advanced rule-based and machine learning models, supporting polarity and verbose output modes.
  name: Deep Categorization API
  slug: deep-categorization-api
- description: Groups a set of texts by thematic similarity, returning clusters with titles, relevance scores, and document lists. Supports multiple clustering modes and custom stopword lists.
  name: Text Clustering API
  slug: text-clustering-api
- description: Semantically tags content for corporate reputation analysis, identifying entities and assigning reputational categories with polarity scores to support brand monitoring use cases.
  name: Corporate Reputation API
  slug: corporate-reputation-api
- description: Automatically extracts a summary from a document by selecting the most relevant sentences, with configurable sentence count output.
  name: Summarization API
  slug: summarization-api
- description: Extracts structural sections from markup documents including title, headings, abstract, and email fields such as from, to, cc, and subject.
  name: Document Structure API
  slug: document-structure-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.meaningcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.meaningcloud.com/developer/apis
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/MeaningCloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meaningcloud
- group: company
  title: ''
  type: Blog
  url: https://www.meaningcloud.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meaningcloud.com/products/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.meaningcloud.com/developer/support
- group: other
  title: ''
  type: X
  url: https://x.com/meaningcloud
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/meaningcloud/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/meaningcloud/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/meaningcloud/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: MeaningCloud is a cloud-based text analytics and natural language processing REST API platform providing sentiment analysis, topic extraction, text classification, language detection, document clustering, corporate reputation analysis, document structure extraction, and deep semantic analysis across multiple languages.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meaningcloud.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: MeaningCloud
nav: Providers
network: true
overview: 'MeaningCloud publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Text Analytics, Natural Language Processing, Sentiment Analysis, Topic Extraction, and Text Classification.


  The MeaningCloud catalog on APIs.io includes 1 JSON-LD context.


  MeaningCloud''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 78
rate_limits:
- limit_count: 6
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 28.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
slug: meaningcloud
tags:
- Text Analytics
- Natural Language Processing
- Sentiment Analysis
- Topic Extraction
- Text Classification
- Language Detection
- NLP
- Semantic Analysis
website: https://www.meaningcloud.com
---
