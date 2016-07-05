#!/usr/bin/env node
 
'use strict'

let lines = require('fs')
				.readFileSync('_chat.txt', 'utf8')
				.split('\r')
				.join('')
				.split('\n')

let chats = {}

for(let line of lines){
	
	if(line 
		&& line.indexOf('changed the subject to') === -1 
		&& line.indexOf('changed this group') === -1
		&& line.indexOf(' added ') === -1
		&& line.indexOf('created this group') === -1
		&& line.indexOf('added you') === -1
		&& line.indexOf('are now secured') === -1
		&& line.indexOf('changed this group ‪') === -1
		&& line.indexOf('HILLEL COMIDITA') === -1
		&& line.indexOf('entrada gratis') === -1
		&& line.indexOf('Javi le falta ese') === -1) {

		let user = line.split(': ')[1]
		let msj = line.split(': ')[2]
		
		if(user) {
			chats[user] ? chats[user] += ' ' + msj : chats[user] = msj
		}
	
	}

}

for(let chat in chats){
	console.log(chats[chat].split(' ').length  + '\t' + chat)
}