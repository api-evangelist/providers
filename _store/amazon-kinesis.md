---
name: Amazon Kinesis
description: Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/amazon-web-services/main/apis/kinesis.yml
created: 2024-01-01T00:00:00.000Z
modified: '2026-04-19'
specificationVersion: '0.18'
tags:
  - Analytics
  - Big Data
  - Data Processing
  - Real-Time
  - Streaming
apis:
  - name: Amazon Kinesis Data Streams
    description: Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. It can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/kinesis/data-streams/
    baseURL: https://kinesis.amazonaws.com
    tags:
      - Data Ingestion
      - Real-Time
      - Streams
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesis/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-kinesis-data-streams-openapi.yml
      - type: AsyncAPI
        url: asyncapi/amazon-kinesis-streams-asyncapi.yml
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
      - type: OpenAPI (Third-Party)
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis/2013-12-02/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-streams/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-streams/getting-started/
      - type: Documentation
        url: https://docs.aws.amazon.com/streams/latest/dev/introduction.html
      - type: Features
        url: https://aws.amazon.com/kinesis/data-streams/features/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/data-streams/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/kinesis/latest/APIReference/
      - type: Quotas
        url: https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
  - name: Amazon Data Firehose
    description: Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to destinations like Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Snowflake, Splunk, and more.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/kinesis/data-firehose/
    baseURL: https://firehose.amazonaws.com
    tags:
      - Data Loading
      - ETL
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/firehose/latest/APIReference/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/firehose/2015-08-04/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-firehose/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-firehose/getting-started/
      - type: Documentation
        url: https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
      - type: Features
        url: https://aws.amazon.com/kinesis/data-firehose/features/
      - type: FAQ
        url: https://aws.amazon.com/firehose/faqs/
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
  - name: Amazon Managed Service for Apache Flink
    description: Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics) is a fully managed service for processing and analyzing streaming data in real time using Apache Flink. You can build applications using Java, Python, Scala, or SQL to transform and analyze streaming data with sub-second latencies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/managed-service-apache-flink/
    baseURL: https://kinesisanalytics.amazonaws.com
    tags:
      - Analytics
      - Apache Flink
      - SQL
      - Stream Processing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/Welcome.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesisanalyticsv2/2018-05-23/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/managed-service-apache-flink/pricing/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html
      - type: Documentation
        url: https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html
      - type: Features
        url: https://aws.amazon.com/managed-service-apache-flink/features/
      - type: FAQ
        url: https://aws.amazon.com/managed-service-apache-flink/faqs/
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
  - name: Amazon Kinesis Video Streams
    description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing. It automatically provisions and elastically scales infrastructure needed to ingest streaming video data from millions of devices.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/kinesis/video-streams/
    baseURL: https://kinesisvideo.amazonaws.com
    tags:
      - IoT
      - Machine Learning
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesisvideo/2017-09-30/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/video-streams/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/video-streams/getting-started/
      - type: APIReference
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html
      - type: Features
        url: https://aws.amazon.com/kinesis/video-streams/features/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/video-streams/faqs/
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
  - name: Amazon Kinesis Video Streams Media
    description: The Amazon Kinesis Video Streams Media API provides operations for reading and writing media data to and from a Kinesis video stream, enabling real-time media ingestion and consumption.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Media.html
    baseURL: https://kinesisvideo.amazonaws.com
    tags:
      - Media
      - Real-Time
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Media.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis-video-media/2017-09-30/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
  - name: Amazon Kinesis Video Streams Archived Media
    description: The Amazon Kinesis Video Streams Archived Media API provides operations for accessing archived video data from Kinesis video streams, including retrieving clips, HLS and DASH streaming session URLs, images, and fragment lists.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Archived_Media.html
    baseURL: https://kinesisvideo.amazonaws.com
    tags:
      - Archived Media
      - DASH
      - HLS
      - Playback
      - Video
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Archived_Media.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis-video-archived-media/2017-09-30/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
  - name: Amazon Kinesis Video Signaling Channels
    description: The Amazon Kinesis Video Signaling Channels API facilitates peer-to-peer WebRTC communication by enabling applications to securely discover each other and exchange connection offers and answers through signaling channels for real-time media streaming.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html
    baseURL: https://kinesisvideo.amazonaws.com
    tags:
      - Real-Time
      - Signaling
      - Video
      - WebRTC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis-video-signaling/2019-12-04/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-kinesis-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-record-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-context.jsonld
common:
  - type: Features
    url: https://aws.amazon.com/kinesis/features/
  - type: FAQ
    url: https://aws.amazon.com/kinesis/data-streams/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/
  - type: Customers
    url: https://aws.amazon.com/kinesis/customers/
  - type: Resources
    url: https://aws.amazon.com/kinesis/resources/
  - type: Documentation
    url: https://docs.aws.amazon.com/kinesis/
  - type: SDK & Tools
    url: https://aws.amazon.com/tools/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Console
    url: https://console.aws.amazon.com/kinesis/
  - type: Firehose Blog
    url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/kinesis-data-firehose/
  - type: Video Streams FAQs
    url: https://aws.amazon.com/kinesis/video-streams/faqs/
  - type: Firehose FAQs
    url: https://aws.amazon.com/firehose/faqs/
  - type: Managed Flink FAQs
    url: https://aws.amazon.com/managed-service-apache-flink/faqs/
  - type: Video Streams Resources
    url: https://aws.amazon.com/kinesis/video-streams/resources/
  - type: Portal
    url: https://aws.amazon.com/kinesis/
  - type: Pricing
    url: https://aws.amazon.com/kinesis/data-streams/pricing/
  - type: Authentication
    url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-iam.html
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/amazon-kinesis
  - type: UseCases
    data:
      - name: Real-Time Analytics
        description: Analyze streaming data for operational metrics and business intelligence.
      - name: Event-Driven Architectures
        description: Build event-driven microservices that react to real-time data streams.
      - name: Machine Learning
        description: Feed real-time data into ML models for online training and inference.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Trigger Lambda functions to process records from Kinesis streams.
      - name: Amazon Kinesis Data Firehose
        description: Use Kinesis streams as source for Firehose delivery.
      - name: Amazon DynamoDB
        description: Store processed streaming records in DynamoDB.
  - type: SpectralRules
    url: rules/amazon-kinesis-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-kinesis-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-kinesis-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
---
