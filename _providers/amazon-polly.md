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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Polly Agentic Access
  operation_count: 15
  slug: amazon-polly-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: The Lexicons API from Amazon Polly — 2 operation(s) for lexicons.
  name: Amazon Polly Lexicons API
  slug: amazon-polly-lexicons-api
- description: The Speech API from Amazon Polly — 1 operation(s) for speech.
  name: Amazon Polly Speech API
  slug: amazon-polly-speech-api
- description: Operations for synthesizing speech from text
  name: Amazon Polly Speech Synthesis API
  slug: amazon-polly-speech-synthesis-api
- description: The SynthesisTasks API from Amazon Polly — 2 operation(s) for synthesistasks.
  name: Amazon Polly SynthesisTasks API
  slug: amazon-polly-synthesistasks-api
- description: The Voices API from Amazon Polly — 1 operation(s) for voices.
  name: Amazon Polly Voices API
  slug: amazon-polly-voices-api
arazzos:
- description: Store a lexicon, start an async synthesis task applying it, then poll to completion.
  name: Amazon Polly Store Lexicon, Start Async Task, and Poll
  slug: amazon-polly-lexicon-async-task-poll-workflow
- description: Store a lexicon, list lexicons, read it back, and delete it.
  name: Amazon Polly Lexicon Lifecycle
  slug: amazon-polly-lexicon-lifecycle-workflow
- description: List synthesis tasks filtered by status, then fetch full detail on the first.
  name: Amazon Polly List Synthesis Tasks and Inspect One
  slug: amazon-polly-list-synthesis-tasks-inspect-workflow
- description: Discover a voice for a language, then start an async synthesis task with it.
  name: Amazon Polly Select Voice and Start Synthesis Task
  slug: amazon-polly-list-voices-start-synthesis-task-workflow
- description: Pick an available voice for a language and synthesize speech with it.
  name: Amazon Polly List Voices and Synthesize Speech
  slug: amazon-polly-list-voices-synthesize-speech-workflow
- description: Page through the full DescribeVoices catalog using the NextToken cursor.
  name: Amazon Polly Paginate the Voice Catalog
  slug: amazon-polly-paginate-voices-workflow
- description: Store a pronunciation lexicon, confirm it, then synthesize speech applying it.
  name: Amazon Polly Store Lexicon and Synthesize With It
  slug: amazon-polly-put-lexicon-synthesize-workflow
- description: Overwrite an existing lexicon, confirm the change, then re-synthesize speech with it.
  name: Amazon Polly Replace Lexicon and Re-synthesize
  slug: amazon-polly-replace-lexicon-resynthesize-workflow
- description: Start an async speech synthesis task, then poll it until it completes.
  name: Amazon Polly Start Synthesis Task and Poll to Completion
  slug: amazon-polly-start-synthesis-task-poll-workflow
artifact_total: 110
collections:
- collection_type: postman
  name: Amazon Polly
  slug: postman-amazon-polly-openapi-original
- collection_type: postman
  name: Amazon Polly API
  slug: postman-amazon-polly
- collection_type: open
  name: Amazon Polly API
  slug: open-amazon-polly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-polly-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-polly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-polly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-polly-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-polly/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-lexicon-async-task-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-lexicon-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-list-synthesis-tasks-inspect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-list-voices-start-synthesis-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-list-voices-synthesize-speech-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-paginate-voices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-put-lexicon-synthesize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-replace-lexicon-resynthesize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-polly-start-synthesis-task-poll-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/polly/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/polly/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/polly/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/polly/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/polly/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/polly/faqs/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-polly
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/polly_code_examples.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-polly-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-polly-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-polly-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-describe-voices-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-engine-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-gender-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-get-lexicon-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-get-speech-synthesis-task-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-language-code-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-lexicon-attributes-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-lexicon-description-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-lexicon-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-list-lexicons-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-list-speech-synthesis-tasks-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-output-format-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-put-lexicon-input-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-speech-mark-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-start-speech-synthesis-task-input-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-start-speech-synthesis-task-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-synthesis-task-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-synthesize-speech-input-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-synthesize-speech-output-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-task-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-text-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-voice-id-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-polly-voice-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-describe-voices-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-engine-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-gender-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-get-lexicon-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-get-speech-synthesis-task-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-language-code-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-lexicon-attributes-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-lexicon-description-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-lexicon-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-list-lexicons-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-list-speech-synthesis-tasks-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-output-format-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-put-lexicon-input-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-speech-mark-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-start-speech-synthesis-task-input-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-start-speech-synthesis-task-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-synthesis-task-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-synthesize-speech-input-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-synthesize-speech-output-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-task-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-text-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-voice-id-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-polly-voice-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-describe-voices-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-get-lexicon-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-get-speech-synthesis-task-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-lexicon-attributes-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-lexicon-description-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-lexicon-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-list-lexicons-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-list-speech-synthesis-tasks-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-put-lexicon-input-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-start-speech-synthesis-task-input-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-start-speech-synthesis-task-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-synthesis-task-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-synthesize-speech-input-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-synthesize-speech-output-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-polly-voice-example.json
created: '2024-01-15'
description: Amazon Polly is a cloud service that converts text into lifelike speech, enabling you to create applications that talk and build entirely new categories of speech-enabled products. Polly supports multiple voices, languages, and audio output formats including neural and generative engines for natural-sounding speech.
examples:
- key_count: 2
  name: Amazon Polly Describe Voices Output Example
  slug: amazon-polly-describe-voices-output-example
- key_count: 9
  name: Amazon Polly Example
  slug: amazon-polly-example
- key_count: 2
  name: Amazon Polly Get Lexicon Output Example
  slug: amazon-polly-get-lexicon-output-example
- key_count: 1
  name: Amazon Polly Get Speech Synthesis Task Output Example
  slug: amazon-polly-get-speech-synthesis-task-output-example
- key_count: 6
  name: Amazon Polly Lexicon Attributes Example
  slug: amazon-polly-lexicon-attributes-example
- key_count: 2
  name: Amazon Polly Lexicon Description Example
  slug: amazon-polly-lexicon-description-example
- key_count: 2
  name: Amazon Polly Lexicon Example
  slug: amazon-polly-lexicon-example
- key_count: 2
  name: Amazon Polly List Lexicons Output Example
  slug: amazon-polly-list-lexicons-output-example
- key_count: 2
  name: Amazon Polly List Speech Synthesis Tasks Output Example
  slug: amazon-polly-list-speech-synthesis-tasks-output-example
- key_count: 1
  name: Amazon Polly Put Lexicon Input Example
  slug: amazon-polly-put-lexicon-input-example
- key_count: 12
  name: Amazon Polly Start Speech Synthesis Task Input Example
  slug: amazon-polly-start-speech-synthesis-task-input-example
- key_count: 1
  name: Amazon Polly Start Speech Synthesis Task Output Example
  slug: amazon-polly-start-speech-synthesis-task-output-example
- key_count: 15
  name: Amazon Polly Synthesis Task Example
  slug: amazon-polly-synthesis-task-example
- key_count: 9
  name: Amazon Polly Synthesize Speech Input Example
  slug: amazon-polly-synthesize-speech-input-example
- key_count: 1
  name: Amazon Polly Synthesize Speech Output Example
  slug: amazon-polly-synthesize-speech-output-example
- key_count: 7
  name: Amazon Polly Voice Example
  slug: amazon-polly-voice-example
features:
- description: Produce natural-sounding speech using neural network-based text-to-speech technology.
  name: Neural Text-to-Speech
- description: New generative engine delivers the highest quality, most human-like speech synthesis.
  name: Generative Engine
- description: Choose from 60+ voices across 30+ languages including male, female, and child voices.
  name: Multiple Voices and Languages
- description: Use Speech Synthesis Markup Language (SSML) to control pronunciation, volume, pitch, and speech rate.
  name: SSML Support
- description: Create custom pronunciation lexicons to control how specific words and phrases are spoken.
  name: Custom Lexicons
- description: Generate speech marks metadata to synchronize spoken text with animations or visual highlights.
  name: Speech Marks
- description: Process large text bodies asynchronously with S3 output for long-form content.
  name: Asynchronous Synthesis Tasks
- description: Output audio in MP3, OGG, PCM, and JSON (speech marks) formats.
  name: Multiple Audio Formats
finops:
- name: Amazon Polly Finops
  service_category: API
  slug: amazon-polly-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Store synthesized speech output from asynchronous synthesis tasks in S3 buckets.
  name: Amazon S3
- description: Combine Polly speech synthesis with Lex conversational AI for voice chatbots.
  name: Amazon Lex
- description: Trigger speech synthesis from Lambda functions for event-driven voice applications.
  name: AWS Lambda
- description: Pair Polly text-to-speech with Transcribe speech-to-text for round-trip voice applications.
  name: Amazon Transcribe
- description: Power Amazon Connect contact center voice responses with Polly neural speech.
  name: Amazon Connect
json_schemas:
- name: DescribeVoicesOutput
  property_count: 2
  slug: amazon-polly-describe-voices-output
- name: Engine
  property_count: 0
  slug: amazon-polly-engine
- name: Gender
  property_count: 0
  slug: amazon-polly-gender
- name: GetLexiconOutput
  property_count: 2
  slug: amazon-polly-get-lexicon-output
- name: GetSpeechSynthesisTaskOutput
  property_count: 1
  slug: amazon-polly-get-speech-synthesis-task-output
- name: LanguageCode
  property_count: 0
  slug: amazon-polly-language-code
- name: LexiconAttributes
  property_count: 6
  slug: amazon-polly-lexicon-attributes
- name: LexiconDescription
  property_count: 2
  slug: amazon-polly-lexicon-description
- name: Lexicon
  property_count: 2
  slug: amazon-polly-lexicon
- name: ListLexiconsOutput
  property_count: 2
  slug: amazon-polly-list-lexicons-output
- name: ListSpeechSynthesisTasksOutput
  property_count: 2
  slug: amazon-polly-list-speech-synthesis-tasks-output
- name: OutputFormat
  property_count: 0
  slug: amazon-polly-output-format
- name: PutLexiconInput
  property_count: 1
  slug: amazon-polly-put-lexicon-input
- name: Amazon Polly Speech Synthesis Definition
  property_count: 9
  slug: amazon-polly
- name: SpeechMarkType
  property_count: 0
  slug: amazon-polly-speech-mark-type
- name: StartSpeechSynthesisTaskInput
  property_count: 12
  slug: amazon-polly-start-speech-synthesis-task-input
- name: StartSpeechSynthesisTaskOutput
  property_count: 1
  slug: amazon-polly-start-speech-synthesis-task-output
- name: SynthesisTask
  property_count: 15
  slug: amazon-polly-synthesis-task
- name: SynthesizeSpeechInput
  property_count: 9
  slug: amazon-polly-synthesize-speech-input
- name: SynthesizeSpeechOutput
  property_count: 1
  slug: amazon-polly-synthesize-speech-output
- name: TaskStatus
  property_count: 0
  slug: amazon-polly-task-status
- name: TextType
  property_count: 0
  slug: amazon-polly-text-type
- name: VoiceId
  property_count: 0
  slug: amazon-polly-voice-id
- name: Voice
  property_count: 7
  slug: amazon-polly-voice
json_structures:
- name: Amazon Polly Describe Voices Output Structure
  property_count: 2
  slug: amazon-polly-describe-voices-output-structure
- name: Amazon Polly Engine Structure
  property_count: 0
  slug: amazon-polly-engine-structure
- name: Amazon Polly Gender Structure
  property_count: 0
  slug: amazon-polly-gender-structure
- name: Amazon Polly Get Lexicon Output Structure
  property_count: 2
  slug: amazon-polly-get-lexicon-output-structure
- name: Amazon Polly Get Speech Synthesis Task Output Structure
  property_count: 1
  slug: amazon-polly-get-speech-synthesis-task-output-structure
- name: Amazon Polly Language Code Structure
  property_count: 0
  slug: amazon-polly-language-code-structure
- name: Amazon Polly Lexicon Attributes Structure
  property_count: 6
  slug: amazon-polly-lexicon-attributes-structure
- name: Amazon Polly Lexicon Description Structure
  property_count: 2
  slug: amazon-polly-lexicon-description-structure
- name: Amazon Polly Lexicon Structure
  property_count: 2
  slug: amazon-polly-lexicon-structure
- name: Amazon Polly List Lexicons Output Structure
  property_count: 2
  slug: amazon-polly-list-lexicons-output-structure
- name: Amazon Polly List Speech Synthesis Tasks Output Structure
  property_count: 2
  slug: amazon-polly-list-speech-synthesis-tasks-output-structure
- name: Amazon Polly Output Format Structure
  property_count: 0
  slug: amazon-polly-output-format-structure
- name: Amazon Polly Put Lexicon Input Structure
  property_count: 1
  slug: amazon-polly-put-lexicon-input-structure
- name: Amazon Polly Speech Mark Type Structure
  property_count: 0
  slug: amazon-polly-speech-mark-type-structure
- name: Amazon Polly Start Speech Synthesis Task Input Structure
  property_count: 12
  slug: amazon-polly-start-speech-synthesis-task-input-structure
- name: Amazon Polly Start Speech Synthesis Task Output Structure
  property_count: 1
  slug: amazon-polly-start-speech-synthesis-task-output-structure
- name: Amazon Polly Structure
  property_count: 9
  slug: amazon-polly-structure
- name: Amazon Polly Synthesis Task Structure
  property_count: 15
  slug: amazon-polly-synthesis-task-structure
- name: Amazon Polly Synthesize Speech Input Structure
  property_count: 9
  slug: amazon-polly-synthesize-speech-input-structure
- name: Amazon Polly Synthesize Speech Output Structure
  property_count: 1
  slug: amazon-polly-synthesize-speech-output-structure
- name: Amazon Polly Task Status Structure
  property_count: 0
  slug: amazon-polly-task-status-structure
- name: Amazon Polly Text Type Structure
  property_count: 0
  slug: amazon-polly-text-type-structure
- name: Amazon Polly Voice Id Structure
  property_count: 0
  slug: amazon-polly-voice-id-structure
- name: Amazon Polly Voice Structure
  property_count: 7
  slug: amazon-polly-voice-structure
jsonld:
- class_count: 16
  name: Amazon Polly Context
  property_count: 36
  slug: amazon-polly-context
layout: provider
modified: '2026-05-19'
name: Amazon Polly
nav: Providers
network: true
overview: 'Amazon Polly publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Lexicons API, Speech API, Speech Synthesis API, and 2 more. Tagged areas include AI, Machine Learning, Speech Synthesis, Text-To-Speech, and TTS.


  The Amazon Polly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Polly''s developer surface includes authentication, developer portal, engineering blog, support, CLI, documentation, pricing, and 91 more developer resources.'
plans:
- name: Amazon Polly Plans Pricing
  plan_count: 3
  slug: amazon-polly-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Amazon Polly Rate Limits
  slug: amazon-polly-rate-limits
rules:
- name: Amazon Polly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-polly-jsonschema-spectral-rules
- name: Amazon Polly API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 11
  slug: amazon-polly-spectral-rules
score:
  band: strong
  composite: 69.8
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 69.6
    developer_ergonomics: 63.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 69.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/screenshots/amazon-polly-2026-06-20T171758.png
security:
- kind: authentication
  name: Amazon Polly Authentication
  slug: amazon-polly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Polly Domain Security
  slug: amazon-polly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Polly Vulnerability Disclosure
  slug: amazon-polly-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-polly
tags:
- AI
- Machine Learning
- Speech Synthesis
- Text-To-Speech
- TTS
- Voice
- SSML
- Neural Engine
- Generative AI
use_cases:
- description: Build conversational interfaces that speak responses to users.
  name: Voice Assistants
- description: Add text-to-speech reading to applications for visually impaired users.
  name: Accessibility Features
- description: Convert written articles and content into audio podcasts automatically.
  name: Podcast and Audio Content
- description: Add spoken narration to educational courses and training materials.
  name: E-Learning Narration
- description: Create interactive voice response systems with natural-sounding speech.
  name: Call Center IVR
- description: Provide native-speaker pronunciation examples for language education.
  name: Language Learning Apps
website: https://console.aws.amazon.com/polly/
---
