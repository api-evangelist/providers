---
name: Amazon Polly
description: Amazon Polly is a cloud service that converts text into lifelike speech, enabling you to create applications that talk and build entirely new categories of speech-enabled products. Polly supports multiple voices, languages, and audio output formats including neural and generative engines for natural-sounding speech.
url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/apis.yml
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AI
  - AWS
  - Machine Learning
  - Speech Synthesis
  - Text-To-Speech
  - TTS
  - Voice
  - SSML
  - Neural Engine
  - Generative AI
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Polly API
    description: The Amazon Polly API enables you to synthesize speech from text (plain text or SSML), manage custom pronunciation lexicons, list available voices across multiple languages and engines, and manage asynchronous synthesis tasks with S3 output.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/polly/
    baseURL: https://polly.amazonaws.com
    tags:
      - Speech Synthesis
      - Text-To-Speech
      - Voice
      - SSML
      - Neural Engine
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/polly/latest/dg/what-is.html
      - type: APIReference
        url: https://docs.aws.amazon.com/polly/latest/dg/API_Reference.html
      - type: OpenAPI
        url: openapi/amazon-polly-openapi.yml
      - type: OpenAPI
        url: openapi/amazon-polly-openapi-original.yaml
      - type: Pricing
        url: https://aws.amazon.com/polly/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/polly/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/polly/faqs/
      - type: Features
        url: https://aws.amazon.com/polly/features/
      - type: Quotas
        url: https://docs.aws.amazon.com/polly/latest/dg/limits.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/polly/latest/dg/limits.html
common:
  - type: Portal
    url: https://console.aws.amazon.com/polly/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/polly/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Documentation
    url: https://docs.aws.amazon.com/polly/
  - type: Pricing
    url: https://aws.amazon.com/polly/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/polly/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/polly/faqs/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-polly
  - type: CodeExamples
    url: https://docs.aws.amazon.com/code-library/latest/ug/polly_code_examples.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: SpectralRules
    url: rules/amazon-polly-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/text-to-speech.yaml
  - type: Vocabulary
    url: vocabulary/amazon-polly-vocabulary.yaml
  - type: Features
    data:
      - name: Neural Text-to-Speech
        description: Produce natural-sounding speech using neural network-based text-to-speech technology.
      - name: Generative Engine
        description: New generative engine delivers the highest quality, most human-like speech synthesis.
      - name: Multiple Voices and Languages
        description: Choose from 60+ voices across 30+ languages including male, female, and child voices.
      - name: SSML Support
        description: Use Speech Synthesis Markup Language (SSML) to control pronunciation, volume, pitch, and speech rate.
      - name: Custom Lexicons
        description: Create custom pronunciation lexicons to control how specific words and phrases are spoken.
      - name: Speech Marks
        description: Generate speech marks metadata to synchronize spoken text with animations or visual highlights.
      - name: Asynchronous Synthesis Tasks
        description: Process large text bodies asynchronously with S3 output for long-form content.
      - name: Multiple Audio Formats
        description: Output audio in MP3, OGG, PCM, and JSON (speech marks) formats.
  - type: UseCases
    data:
      - name: Voice Assistants
        description: Build conversational interfaces that speak responses to users.
      - name: Accessibility Features
        description: Add text-to-speech reading to applications for visually impaired users.
      - name: Podcast and Audio Content
        description: Convert written articles and content into audio podcasts automatically.
      - name: E-Learning Narration
        description: Add spoken narration to educational courses and training materials.
      - name: Call Center IVR
        description: Create interactive voice response systems with natural-sounding speech.
      - name: Language Learning Apps
        description: Provide native-speaker pronunciation examples for language education.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store synthesized speech output from asynchronous synthesis tasks in S3 buckets.
      - name: Amazon Lex
        description: Combine Polly speech synthesis with Lex conversational AI for voice chatbots.
      - name: AWS Lambda
        description: Trigger speech synthesis from Lambda functions for event-driven voice applications.
      - name: Amazon Transcribe
        description: Pair Polly text-to-speech with Transcribe speech-to-text for round-trip voice applications.
      - name: Amazon Connect
        description: Power Amazon Connect contact center voice responses with Polly neural speech.
  - type: JSON-LD
    url: json-ld/amazon-polly-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-polly-describe-voices-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-engine-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-gender-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-get-lexicon-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-get-speech-synthesis-task-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-language-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-lexicon-attributes-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-lexicon-description-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-lexicon-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-list-lexicons-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-list-speech-synthesis-tasks-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-output-format-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-put-lexicon-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-speech-mark-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-start-speech-synthesis-task-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-start-speech-synthesis-task-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-synthesis-task-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-synthesize-speech-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-synthesize-speech-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-task-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-text-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-voice-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-polly-voice-schema.json
  - type: JSONStructure
    url: json-structure/amazon-polly-describe-voices-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-engine-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-gender-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-get-lexicon-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-get-speech-synthesis-task-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-language-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-lexicon-attributes-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-lexicon-description-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-lexicon-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-list-lexicons-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-list-speech-synthesis-tasks-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-output-format-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-put-lexicon-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-speech-mark-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-start-speech-synthesis-task-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-start-speech-synthesis-task-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-synthesis-task-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-synthesize-speech-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-synthesize-speech-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-task-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-text-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-voice-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-polly-voice-structure.json
  - type: Example
    url: examples/amazon-polly-describe-voices-output-example.json
  - type: Example
    url: examples/amazon-polly-example.json
  - type: Example
    url: examples/amazon-polly-get-lexicon-output-example.json
  - type: Example
    url: examples/amazon-polly-get-speech-synthesis-task-output-example.json
  - type: Example
    url: examples/amazon-polly-lexicon-attributes-example.json
  - type: Example
    url: examples/amazon-polly-lexicon-description-example.json
  - type: Example
    url: examples/amazon-polly-lexicon-example.json
  - type: Example
    url: examples/amazon-polly-list-lexicons-output-example.json
  - type: Example
    url: examples/amazon-polly-list-speech-synthesis-tasks-output-example.json
  - type: Example
    url: examples/amazon-polly-put-lexicon-input-example.json
  - type: Example
    url: examples/amazon-polly-start-speech-synthesis-task-input-example.json
  - type: Example
    url: examples/amazon-polly-start-speech-synthesis-task-output-example.json
  - type: Example
    url: examples/amazon-polly-synthesis-task-example.json
  - type: Example
    url: examples/amazon-polly-synthesize-speech-input-example.json
  - type: Example
    url: examples/amazon-polly-synthesize-speech-output-example.json
  - type: Example
    url: examples/amazon-polly-voice-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-polly.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
