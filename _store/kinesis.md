---
aid: kinesis
url: https://raw.githubusercontent.com/api-evangelist/kinesis/refs/heads/main/apis.yml
apis:
- name: Amazon Kinesis Data Streams API
  description: Amazon Kinesis Data Streams is a scalable and durable real-time data streaming service that can continuously capture gigabytes of data per second from hundreds of thousands of sources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kinesis/data-streams/
  baseURL: https://kinesis.{region}.amazonaws.com
  tags:
  - Data Streams
  - Real-Time
  - Streaming
  properties:
  - type: X-documentation
    url: https://docs.aws.amazon.com/kinesis/latest/APIReference/
  - type: X-openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis/2013-12-02/openapi.yaml
  - type: X-pricing
    url: https://aws.amazon.com/kinesis/data-streams/pricing/
  - type: X-getting-started
    url: https://aws.amazon.com/kinesis/data-streams/getting-started/
  - type: X-faq
    url: https://aws.amazon.com/kinesis/data-streams/faqs/
  - type: X-developer-guide
    url: https://docs.aws.amazon.com/streams/latest/dev/introduction.html
  - type: X-security
    url: https://docs.aws.amazon.com/streams/latest/dev/security.html
  - type: X-customers
    url: https://aws.amazon.com/kinesis/data-streams/customers/
  - type: X-integrations
    url: https://aws.amazon.com/kinesis/data-streams/integrations/
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
- name: Amazon Data Firehose API
  description: Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/firehose/
  baseURL: https://firehose.{region}.amazonaws.com
  tags:
  - Data Delivery
  - ETL
  - Streaming
  properties:
  - type: X-documentation
    url: https://docs.aws.amazon.com/firehose/latest/APIReference/
  - type: X-openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/firehose/2015-08-04/openapi.yaml
  - type: X-pricing
    url: https://aws.amazon.com/kinesis/data-firehose/pricing/
  - type: X-getting-started
    url: https://aws.amazon.com/kinesis/data-firehose/getting-started/
  - type: X-faq
    url: https://aws.amazon.com/kinesis/data-firehose/faqs/
  - type: X-developer-guide
    url: https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
- name: Amazon Kinesis Data Analytics API
  description: Amazon Kinesis Data Analytics is the easiest way to analyze streaming data, gain actionable insights, and respond to your business and customer needs in real time.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kinesis/data-analytics/
  baseURL: https://kinesisanalytics.{region}.amazonaws.com
  tags:
  - Analytics
  - Apache Flink
  - SQL
  - Streaming
  properties:
  - type: X-documentation
    url: https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/
  - type: X-openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/kinesisanalyticsv2/2018-05-23/openapi.yaml
  - type: X-pricing
    url: https://aws.amazon.com/kinesis/data-analytics/pricing/
  - type: X-getting-started
    url: https://aws.amazon.com/kinesis/data-analytics/getting-started/
  - type: X-faq
    url: https://aws.amazon.com/kinesis/data-analytics/faqs/
  - type: X-developer-guide
    url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html
  - type: X-security
    url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/security.html
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
- name: Amazon Managed Service for Apache Flink API
  description: Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink) is a fully managed service for processing and analyzing streaming data using Apache Flink. You can use Java, Python, SQL, or Scala to build streaming applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/managed-service-apache-flink/
  baseURL: https://kinesisanalytics.{region}.amazonaws.com
  tags:
  - Analytics
  - Apache Flink
  - Real-Time
  - Streaming
  properties:
  - type: X-documentation
    url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/Welcome.html
  - type: X-developer-guide
    url: https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html
  - type: X-pricing
    url: https://aws.amazon.com/managed-service-apache-flink/pricing/
  - type: X-getting-started
    url: https://aws.amazon.com/managed-service-apache-flink/getting-started/
  - type: X-faq
    url: https://aws.amazon.com/managed-service-apache-flink/faqs/
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
- name: Amazon Kinesis Video Streams API
  description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kinesis/video-streams/
  baseURL: https://kinesisvideo.{region}.amazonaws.com
  tags:
  - IoT
  - Machine Learning
  - Streaming
  - Video
  - WebRTC
  properties:
  - type: X-documentation
    url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html
  - type: X-openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/kinesisvideo/2017-09-30/openapi.yaml
  - type: X-pricing
    url: https://aws.amazon.com/kinesis/video-streams/pricing/
  - type: X-getting-started
    url: https://aws.amazon.com/kinesis/video-streams/getting-started/
  - type: X-faq
    url: https://aws.amazon.com/kinesis/video-streams/faqs/
  - type: X-developer-guide
    url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html
  - type: X-security
    url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security.html
  - type: X-customers
    url: https://aws.amazon.com/kinesis/video-streams/customers/
  - type: X-features
    url: https://aws.amazon.com/kinesis/video-streams/features/
  - type: X-resources
    url: https://aws.amazon.com/kinesis/video-streams/resources/
  - type: X-webrtc-guide
    url: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
name: AWS Kinesis
tags:
- Analytics
- Aws
- Big Data
- Data Processing
- Real-Time
- Streaming
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data so you can get timely insights and react quickly to new information.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

