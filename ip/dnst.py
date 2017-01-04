#--coding:UTF-8--

import dns.resolver

domain = raw_input('Please input an domain: ')
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print j.address


domain = raw_input('Please input an domain: ')
MX = dns.resolver.query(domain,'MX')
for i in MX:
    print 'MX preference =',i.preference,'mail exchanger=',i.exchange

domain = raw_input('Please input an domain: ')
ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()

domain = raw_input('Please input an domain: ')
cname = dns.resolver.query(domain,'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()
