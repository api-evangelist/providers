---
aid: amazon-kinesis-firehose
url: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis-firehose/refs/heads/main/apis.yml
apis:
- name: Amazon Kinesis Data Firehose API
  description: The Amazon Kinesis Data Firehose API provides the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. The API allows you to create and manage delivery streams, configure data transformations using AWS Lambda, set up destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and custom HTTP endpoints, and put records into delivery streams. It automatically scales to match your data throughput with no ongoing administration required.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kinesis/data-firehose/
  baseURL: https://firehose.amazonaws.com
  tags:
  - Analytics
  - AWS
  - Data Delivery
  - Streaming
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/firehose/
  - type: OpenAPI
    url: openapi/amazon-kinesis-firehose-openapi.yml
  - type: Pricing
    url: https://aws.amazon.com/kinesis/data-firehose/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/kinesis/data-firehose/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/kinesis/data-firehose/faqs/
name: Amazon Kinesis Data Firehose
tags:
- Analytics
- AWS
- Data Delivery
- Streaming
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

