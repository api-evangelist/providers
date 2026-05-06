---
aid: smtp
name: SMTP
description: Simple Mail Transfer Protocol (SMTP) is the foundational internet standard for transmitting electronic mail across networks. Defined in RFC 5321 (October 2008), SMTP uses a command-response model over TCP port 25 (or 587 for submission, 465 for SMTPS). It defines commands including EHLO, MAIL FROM, RCPT TO, and DATA, along with a comprehensive set of response codes. SMTP works in conjunction with RFC 5322 (Internet Message Format) which defines the structure of email messages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SMTP
  - Email
  - Internet Standards
  - IETF
  - Messaging
  - Protocols
  - RFC 5321
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/smtp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: smtp:rfc5321
    name: RFC 5321 - Simple Mail Transfer Protocol
    description: RFC 5321 is the IETF standard defining the Simple Mail Transfer Protocol. It specifies the client-server protocol used to transmit email across the internet, including the command set, response codes, session lifecycle, and extension mechanism (ESMTP). Published October 2008, it obsoletes RFC 2821.
    humanURL: https://datatracker.ietf.org/doc/html/rfc5321
    tags:
      - SMTP
      - RFC
      - IETF
      - Email Protocol
      - Standards
    properties:
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc5321
      - type: RFC Editor
        url: https://www.rfc-editor.org/rfc/rfc5321.html
      - type: IETF Datatracker
        url: https://datatracker.ietf.org/doc/rfc5321/
  - aid: smtp:rfc5322
    name: RFC 5322 - Internet Message Format
    description: RFC 5322 defines the format of electronic mail messages transmitted via SMTP. It specifies the syntax for message headers (From, To, Subject, Date, etc.) and body structure. Works in conjunction with RFC 5321.
    humanURL: https://datatracker.ietf.org/doc/html/rfc5322
    tags:
      - Email Format
      - RFC
      - IETF
      - Message Headers
      - Standards
    properties:
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc5322
common:
  - type: IETF RFC
    url: https://datatracker.ietf.org/doc/html/rfc5321
  - type: RFC Editor
    url: https://www.rfc-editor.org/rfc/rfc5321.html
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
  - type: Related Standard
    url: https://datatracker.ietf.org/doc/html/rfc5322
  - type: Related Standard
    url: https://datatracker.ietf.org/doc/html/rfc3463
  - type: Related Standard
    url: https://datatracker.ietf.org/doc/html/rfc4409
  - type: IETF Working Group
    url: https://datatracker.ietf.org/wg/emailcore/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
