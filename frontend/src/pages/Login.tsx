import '@css/Auth.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { faGoogle, faLinkedinIn, faGithub, faFacebookF, faApple } from '@fortawesome/free-brands-svg-icons'

function Login() {
    return (
        <div className="relative min-h-screen">
            <div className="absolute inset-0 bg-cover bg-center blur-lg scale-105 bg-linear-to-br
            from-fs-green to-fs-yellow"/>

            <div className="relative z-10 flex items-center justify-center min-h-screen">
                <div className="bg-white rounded-xl shadow-md p-10 flex flex-col gap-3 w-full max-w-lg my-40">
                    <div className="flex justify-center space-x-1 mt-6">
                        <FontAwesomeIcon icon={faHeart} className="text-center text-fs-purple text-4xl -rotate-90"/>
                        <FontAwesomeIcon icon={faHeart} className="text-center text-fs-yellow text-4xl"/>
                        <FontAwesomeIcon icon={faHeart} className="text-center text-fs-green text-4xl rotate-90"/>
                    </div>
                    <h2 className="text-black text-center text-2xl font-bold">Welcome Back!</h2>
                    <p className="text-center text-gray-500 text-sm">Log in to continue your advising journey.</p>
                    <p className="text-base text-black font-semibold mt-4">Email or username</p>
                    <input className="border p-2 rounded-lg caret-fs-purple text-black"></input>
                    <p className="text-base text-black font-semibold mt-4">Password</p>
                    <input className="border p-2 rounded-lg caret-fs-purple text-black" type="password"></input>
                    <p className="text-fs-green text-small underline">Forgot Password</p>
                    <button className="bg-fs-purple text-white font-bold py-2 rounded my-6 ">Login</button>
                    <div className="flex items-center before:h-px before:flex-1 before:bg-zinc-600 after:h-px after:flex-1
                    after:bg-zinc-600">
                        <p className="mx-4 text-zinc-600">or</p>
                    </div>
                    <div className="flex flex-row space-x-4 mx-6 mt-4 justify-center">
                        <div className="flex size-12 rounded-full bg-red-500 items-center justify-center">
                            <FontAwesomeIcon icon={faGoogle} className="text-white text-3xl"/>
                        </div>
                        <div className="flex size-12 rounded-full bg-blue-500 items-center justify-center">
                            <FontAwesomeIcon icon={faLinkedinIn} className="text-white text-2xl"/>
                        </div>
                        <div className="flex size-12 rounded-full bg-black items-center justify-center">
                            <FontAwesomeIcon icon={faGithub} className="text-white text-3xl"/>
                        </div>
                        <div className="flex size-12 rounded-full bg-blue-500 items-center justify-center">
                            <FontAwesomeIcon icon={faFacebookF} className="text-white text-2xl"/>
                        </div>
                        <div className="flex size-12 rounded-full bg-black items-center justify-center">
                            <FontAwesomeIcon icon={faApple} className="text-white text-3xl"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Login