---
aid: kinesis
name: AWS Kinesis
description: Amazon Kinesis is a family of fully managed AWS services for collecting, processing, and analyzing real-time streaming data. The family includes Kinesis Data Streams for scalable record ingestion, Amazon Data Firehose (formerly Kinesis Data Firehose) for delivery to data lakes and analytics destinations, Amazon Managed Service for Apache Flink (formerly Kinesis Data Analytics) for stateful stream processing, and Kinesis Video Streams for ingest and playback of media from connected devices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Apache Flink
  - AWS
  - Big Data
  - Data Processing
  - Real-Time
  - Streaming
  - Video
url: https://raw.githubusercontent.com/api-evangelist/kinesis/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kinesis:data-streams-api
    name: Amazon Kinesis Data Streams API
    description: Amazon Kinesis Data Streams is a scalable and durable real-time data streaming service that can continuously capture gigabytes of data per second from hundreds of thousands of sources. The API supports stream creation and lifecycle management, record put and get operations, shard discovery and resharding, enhanced fan-out consumers, and stream consumer registration for downstream processing.
    humanURL: https://aws.amazon.com/kinesis/data-streams/
    baseURL: https://kinesis.{region}.amazonaws.com
    tags:
      - Data Streams
      - Ingestion
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesis/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-kinesis-data-streams-openapi-original.yml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-streams/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-streams/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/data-streams/faqs/
      - type: DeveloperGuide
        url: https://docs.aws.amazon.com/streams/latest/dev/introduction.html
      - type: Security
        url: https://docs.aws.amazon.com/streams/latest/dev/security.html
      - type: Customers
        url: https://aws.amazon.com/kinesis/data-streams/customers/
      - type: Integrations
        url: https://aws.amazon.com/kinesis/data-streams/integrations/
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
  - aid: kinesis:data-firehose-api
    name: Amazon Data Firehose API
    description: Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. Firehose can capture, transform with Lambda or built-in conversions, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and supported partner destinations with automatic scaling and retry handling.
    humanURL: https://aws.amazon.com/firehose/
    baseURL: https://firehose.{region}.amazonaws.com
    tags:
      - Data Delivery
      - ETL
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/firehose/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-data-firehose-openapi-original.yml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-firehose/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-firehose/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/data-firehose/faqs/
      - type: DeveloperGuide
        url: https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
  - aid: kinesis:data-analytics-api
    name: Amazon Kinesis Data Analytics API
    description: Amazon Kinesis Data Analytics is a managed service for analyzing streaming data using SQL or Apache Flink. The API enables creation and management of streaming applications, input and output stream configuration, application code deployment, and runtime monitoring, enabling near real-time insights and event-driven actions on continuously arriving data.
    humanURL: https://aws.amazon.com/kinesis/data-analytics/
    baseURL: https://kinesisanalytics.{region}.amazonaws.com
    tags:
      - Analytics
      - Apache Flink
      - SQL
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/
      - type: OpenAPI
        url: openapi/amazon-kinesis-data-analytics-openapi-original.yml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-analytics/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-analytics/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/data-analytics/faqs/
      - type: DeveloperGuide
        url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html
      - type: Security
        url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/security.html
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
  - aid: kinesis:managed-flink-api
    name: Amazon Managed Service for Apache Flink API
    description: Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink) is a fully managed service for processing and analyzing streaming data using Apache Flink. Developers build streaming applications in Java, Python, SQL, or Scala, and the service handles infrastructure provisioning, scaling, state management, and high availability for stateful stream processing.
    humanURL: https://aws.amazon.com/managed-service-apache-flink/
    baseURL: https://kinesisanalytics.{region}.amazonaws.com
    tags:
      - Analytics
      - Apache Flink
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/Welcome.html
      - type: DeveloperGuide
        url: https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/managed-service-apache-flink/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/managed-service-apache-flink/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/managed-service-apache-flink/faqs/
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
  - aid: kinesis:video-streams-api
    name: Amazon Kinesis Video Streams API
    description: Amazon Kinesis Video Streams makes it easy to securely stream video, audio, and time-encoded data from connected devices to AWS for analytics, machine learning, playback, and other processing. The API supports stream lifecycle management, media ingest and retrieval, HLS and DASH playback URL generation, signaling for WebRTC peer connections, and integration with AWS Rekognition for video analysis.
    humanURL: https://aws.amazon.com/kinesis/video-streams/
    baseURL: https://kinesisvideo.{region}.amazonaws.com
    tags:
      - IoT
      - Machine Learning
      - Streaming
      - Video
      - WebRTC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html
      - type: OpenAPI
        url: openapi/amazon-kinesis-video-streams-openapi-original.yml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/video-streams/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/video-streams/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/video-streams/faqs/
      - type: DeveloperGuide
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html
      - type: Security
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security.html
      - type: Customers
        url: https://aws.amazon.com/kinesis/video-streams/customers/
      - type: Features
        url: https://aws.amazon.com/kinesis/video-streams/features/
      - type: Resources
        url: https://aws.amazon.com/kinesis/video-streams/resources/
      - type: WebRTCGuide
        url: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
common:
  - type: Website
    url: https://aws.amazon.com/kinesis/
  - type: Documentation
    url: https://docs.aws.amazon.com/kinesis/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/
  - type: Console
    url: https://console.aws.amazon.com/kinesis/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SLA
    url: https://aws.amazon.com/kinesis/sla/
  - type: GettingStarted
    url: https://aws.amazon.com/kinesis/getting-started/
  - type: Legal
    url: https://aws.amazon.com/legal/service-level-agreements/
  - type: Contact
    url: https://aws.amazon.com/contact-us/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
