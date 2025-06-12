# cliente_ruby.rb
require 'socket'

host = '127.0.0.1'
port = 5000

begin
  socket = TCPSocket.new(host, port)
  print "Digite um nome para enviar ao servidor: "
  nome = gets.chomp
  socket.puts(nome)
  puts "Nome enviado com sucesso!"
ensure
  socket.close if socket
end
