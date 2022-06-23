const addAnotherUser = document.querySelector('#add-another-user')
const paidUsers = document.querySelector('.paid-users')
const paidUser = document.querySelector('.paid-user')
const toggleNavMenu = document.querySelector('#toggle-nav-menu')
const navMenu = document.querySelector('.nav')
const price = document.querySelector('#price')
const count = document.querySelector('#count')
const total = document.querySelector('.total')
const paidUsersInTable = document.querySelectorAll('.paid-user-table')
const allUsers = document.querySelectorAll('.all-users')
const userTotalPaid = document.querySelectorAll('.user-total-paid')
const whoOwesToWhom = document.querySelector('.who-owes-to-whom')


const left = document.querySelector('.left')
let userPaidInput = document.querySelectorAll('.user-paid-input')


let unique = 1

toggleNavMenu.onclick = () => {
	console.log('clicked')
	if (navMenu.style.display === 'none' || navMenu.style.display === '') {
		navMenu.style.animation = "slidein .4s"
		console.log('if none')
		navMenu.style.display = 'block'
	} else {
		console.log('if block')
		navMenu.style.animation = "slideout .4s"
		setTimeout(function() {
			console.log(window.innerWidth)
			if (window.innerWidth <= 768) {
				console.log('setTimeout')
				navMenu.style.display = 'none'
			}
		}, 300)
	}
}

setInterval(() => {
	if (window.innerWidth >= 768) {
		navMenu.style.display = 'block'
		navMenu.style.animation = 'none'
	}
}, 100)

addAnotherUser.onclick = () => {
	const newPaidUser = paidUser.cloneNode(true)
	const selectUser = newPaidUser.querySelector('#select-user')
	const paid = newPaidUser.querySelector('#paid')
	const deleteButton = document.createElement('input')

	selectUser.id += `-${unique}`
	paid.id += `-${unique}`
	paid.value = ''

	unique++

	deleteButton.type = 'button'
	deleteButton.classList += 'delete-added-user'
	deleteButton.value = 'Delete User'


	newPaidUser.append(deleteButton)
	paidUsers.append(newPaidUser)
}

setInterval(() => {
	const deleteAddedUsers = document.querySelectorAll('.delete-added-user')
	deleteAddedUsers.forEach(deleteAddedUser => {
		deleteAddedUser.onclick = () => {
			deleteAddedUser.parentNode.remove()
		}}
	)
}, 800)

setInterval(() =>  total.innerHTML = price.value * count.value, 800)
setInterval(() => {
	let totalPaid = 0

	userPaidInput = paidUsers.querySelectorAll('.user-paid-input')

	// console.log(userPaidInput)
	userPaidInput.forEach(paid => {
		paid = paid.value || 0
		totalPaid += parseInt(paid)
	})
	// console.log(totalPaid)
	left.innerHTML = price.value * count.value - totalPaid

}, 800)

allUsers.forEach(user => {
	let userTotalPaid = 0
	paidUsersInTable.forEach(paidUser => {
		// console.log(user)
		// console.log(user.textContent.toLowerCase())
		if (paidUser.dataset.user === user.textContent.toLowerCase()) {
			// console.log(user.textContent, '-----------------------')
			// console.log(paidUser.textContent.replaceAll(/\s/g,''))
			let myExpense = paidUser.textContent.replaceAll(/\s/g,'')
			// console.log(typeof(myExpense), myExpense)
			// console.log(parseFloat(myExpense))

			// userTotalPaid += myExpense
		}
	})
	// console.log(userTotalPaid)
	userTotalPaid = 0
})

userTotalPaidList = []
userTotalPaid.forEach(user => {
	console.log(user.outerText)
	userTotalPaidList.push({
		username: user.dataset.user,
		total: user.outerText
	})

	console.log(userTotalPaidList)
})

userTotalPaidList.sort((user_1, user_2) => user_2.total - user_1.total)
console.log(userTotalPaidList[0])

userTotalPaidList.slice(1).forEach(element => {
	console.log(element)
	const p = document.createElement('p')
	p.innerHTML = `${element.username} should give to ${userTotalPaidList[0].username}: ${userTotalPaidList[0].total - element.total}`
	whoOwesToWhom.append(p)
	
})
// Lowest to highest
// let lowestToHighest = userTotalPaid.sort((a, b) => a - b);