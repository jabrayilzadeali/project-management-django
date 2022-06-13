const addAnotherUser = document.querySelector('#add-another-user')
const paidUsers = document.querySelector('.paid-users')
const paidUser = document.querySelector('.paid-user')
const toggleNavMenu = document.querySelector('#toggle-nav-menu')
const navMenu = document.querySelector('.nav')
const price = document.querySelector('#price')
const count = document.querySelector('#count')
const total = document.querySelector('.total')


const left = document.querySelector('.left')
let userPaidInput = document.querySelectorAll('.user-paid-input')

console.log(navMenu.style)
console.log(window.innerWidth)

let unique = 1

toggleNavMenu.onclick = () => {
	console.log('clicked')
	// alert('okay')
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
	// deleteButton.onclick = () => {
	// 	newPaidUser.remove()
	// }
}

setInterval(() => {
	const deleteAddedUsers = document.querySelectorAll('.delete-added-user')
	deleteAddedUsers.forEach(deleteAddedUser => {
		deleteAddedUser.onclick = () => {
			console.log('I am trying to delete you')
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