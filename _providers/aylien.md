---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Aylien Agentic Access
  operation_count: 20
  slug: aylien-agentic-access
  summary_line: 20 operations · 2 acting
api_count: 17
apis:
- description: The Absa API from AYLIEN — 1 operation(s) for absa.
  name: AYLIEN Absa API
  slug: aylien-absa-api
- description: The autocomplete API from AYLIEN — 1 operation(s) for autocomplete.
  name: AYLIEN autocomplete API
  slug: aylien-autocomplete-api
- description: The Classify API from AYLIEN — 2 operation(s) for classify.
  name: AYLIEN Classify API
  slug: aylien-classify-api
- description: The cluster API from AYLIEN — 1 operation(s) for cluster.
  name: AYLIEN cluster API
  slug: aylien-cluster-api
- description: The Concepts API from AYLIEN — 1 operation(s) for concepts.
  name: AYLIEN Concepts API
  slug: aylien-concepts-api
- description: The Elsa API from AYLIEN — 1 operation(s) for elsa.
  name: AYLIEN Elsa API
  slug: aylien-elsa-api
- description: The Entities API from AYLIEN — 1 operation(s) for entities.
  name: AYLIEN Entities API
  slug: aylien-entities-api
- description: The Extract API from AYLIEN — 1 operation(s) for extract.
  name: AYLIEN Extract API
  slug: aylien-extract-api
- description: The Hashtags API from AYLIEN — 1 operation(s) for hashtags.
  name: AYLIEN Hashtags API
  slug: aylien-hashtags-api
- description: The histogram API from AYLIEN — 1 operation(s) for histogram.
  name: AYLIEN histogram API
  slug: aylien-histogram-api
- description: The Language API from AYLIEN — 1 operation(s) for language.
  name: AYLIEN Language API
  slug: aylien-language-api
- description: The related_story API from AYLIEN — 1 operation(s) for related_story.
  name: AYLIEN related_story API
  slug: aylien-related-story-api
- description: The Sentiment API from AYLIEN — 1 operation(s) for sentiment.
  name: AYLIEN Sentiment API
  slug: aylien-sentiment-api
- description: The story API from AYLIEN — 1 operation(s) for story.
  name: AYLIEN story API
  slug: aylien-story-api
- description: The Summarize API from AYLIEN — 1 operation(s) for summarize.
  name: AYLIEN Summarize API
  slug: aylien-summarize-api
- description: The time_series API from AYLIEN — 1 operation(s) for time_series.
  name: AYLIEN time_series API
  slug: aylien-time-series-api
- description: The trends API from AYLIEN — 1 operation(s) for trends.
  name: AYLIEN trends API
  slug: aylien-trends-api
artifact_total: 107
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aylien-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aylien-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aylien-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aylien.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aylien.com/newsapi/v6/getting-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/AYLIEN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aylien
- group: company
  title: ''
  type: Blog
  url: https://aylien.com/blog/general
- group: commercial
  title: ''
  type: Pricing
  url: https://aylien.com/product/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://aylien.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/aylien
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/aylien/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/aylien/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/aylien/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: AYLIEN is a news intelligence and text analysis platform providing REST APIs for article extraction, sentiment analysis, entity recognition, summarization, concept detection, and NLP-enriched news aggregation from over 80,000 public and licensed sources delivering 1.4 million articles daily. Now part of Quantexa, AYLIEN enables developers, data scientists, and risk analysts to build intelligent applications powered by global news intelligence.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aylien.png
json_schemas:
- name: AggregatedSentiment
  property_count: 3
  slug: news-api-AggregatedSentiment
- name: Author
  property_count: 3
  slug: news-api-Author
- name: Autocomplete
  property_count: 2
  slug: news-api-Autocomplete
- name: Autocompletes
  property_count: 1
  slug: news-api-Autocompletes
- name: Category
  property_count: 7
  slug: news-api-Category
- name: CategoryLinks
  property_count: 2
  slug: news-api-CategoryLinks
- name: CategoryTaxonomy
  property_count: 0
  slug: news-api-CategoryTaxonomy
- name: Cluster
  property_count: 7
  slug: news-api-Cluster
- name: Clusters
  property_count: 3
  slug: news-api-Clusters
- name: Entities
  property_count: 2
  slug: news-api-Entities
- name: Entity
  property_count: 8
  slug: news-api-Entity
- name: EntityLinks
  property_count: 3
  slug: news-api-EntityLinks
- name: EntitySentiment
  property_count: 2
  slug: news-api-EntitySentiment
- name: EntitySurfaceForm
  property_count: 2
  slug: news-api-EntitySurfaceForm
- name: Error
  property_count: 6
  slug: news-api-Error
- name: ErrorLinks
  property_count: 2
  slug: news-api-ErrorLinks
- name: Errors
  property_count: 1
  slug: news-api-Errors
- name: HistogramInterval
  property_count: 2
  slug: news-api-HistogramInterval
- name: Histograms
  property_count: 7
  slug: news-api-Histograms
- name: Location
  property_count: 3
  slug: news-api-Location
- name: Logical operators
  property_count: 0
  slug: news-api-Logical
- name: One of the logical operators such as $and, $or, $not
  property_count: 3
  slug: news-api-Logicals
- name: Media
  property_count: 6
  slug: news-api-Media
- name: MediaFormat
  property_count: 0
  slug: news-api-MediaFormat
- name: MediaType
  property_count: 0
  slug: news-api-MediaType
- name: To perform a nested search on entities use this.
  property_count: 9
  slug: news-api-NestedEntity
- name: Query defines the search query on a field
  property_count: 56
  slug: news-api-Parameter
- name: Query defines the search query on a field
  property_count: 8
  slug: news-api-Query
- name: Rank
  property_count: 3
  slug: news-api-Rank
- name: Rankings
  property_count: 1
  slug: news-api-Rankings
- name: RelatedStories
  property_count: 6
  slug: news-api-RelatedStories
- name: RepresentativeStory
  property_count: 4
  slug: news-api-RepresentativeStory
- name: Scope
  property_count: 4
  slug: news-api-Scope
- name: ScopeLevel
  property_count: 0
  slug: news-api-ScopeLevel
- name: Sentiment
  property_count: 2
  slug: news-api-Sentiment
- name: SentimentPolarity
  property_count: 0
  slug: news-api-SentimentPolarity
- name: Sentiments
  property_count: 2
  slug: news-api-Sentiments
- name: ShareCount
  property_count: 2
  slug: news-api-ShareCount
- name: ShareCounts
  property_count: 4
  slug: news-api-ShareCounts
- name: Source
  property_count: 11
  slug: news-api-Source
- name: Stories
  property_count: 5
  slug: news-api-Stories
- name: Story
  property_count: 23
  slug: news-api-Story
- name: StoryCluster
  property_count: 5
  slug: news-api-StoryCluster
- name: StoryLinks
  property_count: 4
  slug: news-api-StoryLinks
- name: StoryTranslation
  property_count: 2
  slug: news-api-StoryTranslation
- name: StoryTranslations
  property_count: 1
  slug: news-api-StoryTranslations
- name: Summary
  property_count: 1
  slug: news-api-Summary
- name: TimeSeries
  property_count: 3
  slug: news-api-TimeSeries
- name: TimeSeriesList
  property_count: 4
  slug: news-api-TimeSeriesList
- name: Trend
  property_count: 3
  slug: news-api-Trend
- name: Trends
  property_count: 4
  slug: news-api-Trends
- name: Warning
  property_count: 3
  slug: news-api-Warning
- name: Article
  property_count: 8
  slug: text-api-Article
- name: AspectSentiment
  property_count: 4
  slug: text-api-AspectSentiment
- name: AspectSentimentAspect
  property_count: 6
  slug: text-api-AspectSentimentAspect
- name: AspectSentimentSentence
  property_count: 4
  slug: text-api-AspectSentimentSentence
- name: AspectSentimentSentenceAspect
  property_count: 4
  slug: text-api-AspectSentimentSentenceAspect
- name: Classification
  property_count: 4
  slug: text-api-Classification
- name: ClassificationCategory
  property_count: 5
  slug: text-api-ClassificationCategory
- name: Concept
  property_count: 3
  slug: text-api-Concept
- name: Concepts
  property_count: 3
  slug: text-api-Concepts
- name: Entities
  property_count: 3
  slug: text-api-Entities
- name: EntitySentiment
  property_count: 2
  slug: text-api-EntitySentiment
- name: EntitySentimentEntity
  property_count: 4
  slug: text-api-EntitySentimentEntity
- name: EntitySentimentEntityLink
  property_count: 4
  slug: text-api-EntitySentimentEntityLink
- name: EntitySentimentEntityMention
  property_count: 4
  slug: text-api-EntitySentimentEntityMention
- name: Error
  property_count: 6
  slug: text-api-Error
- name: ErrorLinks
  property_count: 1
  slug: text-api-ErrorLinks
- name: Errors
  property_count: 1
  slug: text-api-Errors
- name: GenericAspect
  property_count: 0
  slug: text-api-GenericAspect
- name: GenericAspectConfidence
  property_count: 0
  slug: text-api-GenericAspectConfidence
- name: GenericConfidence
  property_count: 0
  slug: text-api-GenericConfidence
- name: GenericInputLanguage
  property_count: 0
  slug: text-api-GenericInputLanguage
- name: GenericInputText
  property_count: 0
  slug: text-api-GenericInputText
- name: GenericPolarity
  property_count: 0
  slug: text-api-GenericPolarity
- name: GenericPolarityConfidence
  property_count: 0
  slug: text-api-GenericPolarityConfidence
- name: Hashtags
  property_count: 3
  slug: text-api-Hashtags
- name: Language
  property_count: 3
  slug: text-api-Language
- name: Sentiment
  property_count: 5
  slug: text-api-Sentiment
- name: Summary
  property_count: 2
  slug: text-api-Summary
- name: SurfaceForm
  property_count: 3
  slug: text-api-SurfaceForm
jsonld:
- class_count: 0
  name: News Api Context
  property_count: 0
  slug: news-api
- class_count: 0
  name: Text Api Context
  property_count: 0
  slug: text-api
layout: provider
modified: '2026-06-13'
name: AYLIEN
nav: Providers
network: true
overview: 'AYLIEN publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Absa API, autocomplete API, Classify API, and 14 more. Tagged areas include News Intelligence, Text Analysis, NLP, Sentiment Analysis, and Entity Recognition.


  The AYLIEN catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  AYLIEN''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 42
rate_limits:
- limit_count: 5
  name: Rate Limits
  slug: rate-limits
rules:
- name: AYLIEN API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aylien-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Aylien Authentication
  slug: aylien-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Aylien Domain Security
  slug: aylien-domain-security
  summary_line: no transport/DNS hardening detected
slug: aylien
tags:
- News Intelligence
- Text Analysis
- NLP
- Sentiment Analysis
- Entity Recognition
- Natural Language Processing
- News API
- Article Extraction
- Summarization
- Concept Detection
website: https://aylien.com
---
