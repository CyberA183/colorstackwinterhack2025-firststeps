import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faUserPlus, faLeaf } from '@fortawesome/free-solid-svg-icons'
import { NavLink, Link } from 'react-router-dom'

export default function NavigationBar() {

    const navigation = [
        {name: "Home", href: "/"},
        {name: "About", href: "/about"},
        {name: "Product", href: "/product"}
    ]

    const buttons = [
    {label: "Login", icon: faUser, href:"/login", styles: "bg-fs-yellow text-fs-purple hover:bg-yellow-400"},
    {label: "Register", icon: faUserPlus, href: "/register", styles: "bg-fs-purple text-fs-yellow hover:bg-purple-400"}
    ]

    return (
        <header className="fixed top-0 w-full bg-transparent duration-300">
            <nav className="flex items-center px-6">
                <FontAwesomeIcon icon={faLeaf} className="m-2 px-4 text-3xl transition-transform duration-300
                hover:text-fs-purple hover:scale-110" />
                <div className="flex space-x-4 mx-auto">
                    {navigation.map((item) => (
                        <NavLink
                            key={item.name}
                            to={item.href}
                            className={({ isActive }) => `font-pt px-6 py-10 text-medium font-medium ${
                                isActive ? "text-white underline underline-offset-8 decoration-fs-yellow" :
                                "text-gray-300 hover:text-fs-yellow"
                            }`}
                        >
                            {item.name}
                        </NavLink>
                    ))}
                </div>
                <div className="flex items-center space-x-6">
                    {buttons.map((button) => (
                        <Link
                            key={button.label}
                            to={button.href}
                            className={`group flex items-center rounded-full px-6 py-3
                                font-bold shadow-md transition-all duration-300 hover:shadow-lg
                                hover:-translate-y-0.5 ${button.styles}`}
                        >
                        <FontAwesomeIcon icon={button.icon} className="mr-2 transition-transform duration-300 group-hover:scale-110" />
                        {button.label}
                        </Link>
                    ))}
                </div>
            </nav>
        </header>

    )

}