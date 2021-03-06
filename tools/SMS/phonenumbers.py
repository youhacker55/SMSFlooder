#!/usr/bin/env python3

from phonenumbers import geocoder, parse


def normalize(phone):
    if phone[0] == "+":
        phone = phone[1:]
    return phone


def transformPhone(phone, i):
	if i == 5:
		return '+' + phone[0] + ' (' + phone[1:4] + ') ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]


def getCountry(phone):
	query = parse("+" + phone, None)
	return repr(geocoder.description_for_number(query, 'en'))
