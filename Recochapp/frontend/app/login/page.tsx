'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { ArrowRight, Mail, Lock, Loader2, AlertCircle } from 'lucide-react'

export default function Login() {
  const router = useRouter()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      // Usamos URLSearchParams porque OAuth2PasswordRequestForm espera form-data
      const formData = new URLSearchParams()
      formData.append('username', email)
      formData.append('password', password)

      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1'}/login/access-token`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData,
      })

      if (!res.ok) {
        throw new Error('Credenciales incorrectas, parcero.')
      }

      const data = await res.json()
      
      // Guardamos el token (en un app real usaríamos cookies seguras o next-auth)
      localStorage.setItem('token', data.access_token)
      
      // Redirigir al dashboard (o home por ahora)
      router.push('/')
      
    } catch (err: any) {
      setError(err.message || 'Algo salió mal')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-recocha-dark p-4 text-white">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h2 className="mt-6 text-3xl font-extrabold tracking-tight text-white">
            Inicia sesión
          </h2>
          <p className="mt-2 text-sm text-gray-400">
            ¿No tienes cuenta?{' '}
            <Link href="/register" className="font-medium text-recocha-neon hover:text-green-400">
              Regístrate aquí
            </Link>
          </p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md shadow-sm">
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-500">
                <Mail size={20} />
              </div>
              <input
                type="email"
                required
                className="block w-full rounded-md border-0 bg-recocha-gray py-3 pl-10 text-white placeholder:text-gray-500 focus:ring-2 focus:ring-recocha-neon sm:text-sm"
                placeholder="Correo electrónico"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-500">
                <Lock size={20} />
              </div>
              <input
                type="password"
                required
                className="block w-full rounded-md border-0 bg-recocha-gray py-3 pl-10 text-white placeholder:text-gray-500 focus:ring-2 focus:ring-recocha-neon sm:text-sm"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          {error && (
            <div className="flex items-center gap-2 text-red-400 text-sm bg-red-900/20 p-3 rounded">
              <AlertCircle size={16} /> {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="group relative flex w-full justify-center rounded-md bg-recocha-neon px-3 py-3 text-sm font-bold text-black hover:bg-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-recocha-neon disabled:opacity-70 transition-all"
          >
            {loading ? <Loader2 className="animate-spin" /> : 'Entrar a la cancha'}
            {!loading && <ArrowRight className="ml-2 h-4 w-4" />}
          </button>
        </form>
      </div>
    </div>
  )
}